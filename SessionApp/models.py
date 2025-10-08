from django.db import models
from ConferenceApp.models import Conference
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.
name_validator = RegexValidator(
    regex='^[a-zA-Z\s-]+$',
    message="ce champ ne doit contenir que des lettres"
)
class Session(models.Model):
    session_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=250)
    session_day=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.CharField(max_length=255,validators=[name_validator])
    created_at=models.DateTimeField(auto_now_add=True)  
    update_at=models.DateTimeField(auto_now=True)
    #conference=models.ForeignKey("ConferenceApp.Conference")
    conference=models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="sessions")

    def clean(self):
        if self.conference:
            if not (self.conference.start_date <= self.session_day <= self.conference.end_date):
                raise ValidationError({
                    'session_day': f"La date de la session ({self.session_day}) doit être comprise entre "
                                   f"{self.conference.start_date} et {self.conference.end_date}."
                })

        # Vérifier que l’heure de fin est supérieure à celle de début
        if self.end_time <= self.start_time:
            raise ValidationError({
                'end_time': "L'heure de fin doit être supérieure à l'heure de début."
            })

    def save(self, *args, **kwargs):
        # Appelle la validation avant la sauvegarde
        self.full_clean()
        super().save(*args, **kwargs)

    