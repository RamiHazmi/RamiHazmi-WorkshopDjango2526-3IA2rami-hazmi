from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import random, string


# Create your models here.
title_validator = RegexValidator(
    regex='^[a-zA-Z\s-]+$',
    message="ce champ ne doit contenir que des lettres"
)
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

class Conference(models.Model):
    conference_id = models.AutoField(primary_key=True)  # int primary key
    name = models.CharField(max_length=255, validators=[title_validator])  # varchar
    
    THEME = [
        ("IA", "Computer science & ia"),
        ("SE", "Science & Engineering"),
        ("SC", "Social Sciences & Education"),
        ("IT", "Interdisciplinary Themes."),
    ]
    
    location = models.CharField(max_length=50)
    description = models.TextField(
        validators=[MinLengthValidator(30, message="Vous devez saisir au moins 30 caractères")]
    )
    start_date = models.DateField()  # date
    end_date = models.DateField()    # date
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Vérifie que les dates existent avant de comparer
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("La date de début doit être antérieure à la date de fin")

class Submission(models.Model):
    Submission_id = models.CharField(max_length=255, primary_key=True, unique=True)
    title = models.CharField(max_length=50)
    abstract = models.TextField()

    # ✅ keywords : vérifier qu’il ne dépasse pas 10 mots-clés (séparés par des virgules)
    keywords = models.TextField()

    # ✅ paper : autoriser uniquement les fichiers PDF
    paper = models.FileField(
        upload_to="paper/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
    )

    STATUS = [
        ("submitted", "submitted"),
        ("under review", "under review"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]

    status = models.CharField(max_length=50, choices=STATUS)
    payed = models.BooleanField(default=False)
    Submission_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey("UserApp.User", on_delete=models.CASCADE, related_name="submissions")
    Conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="submissions")


    def clean(self):
        # ✅ 1. Vérifier que la conférence est à venir
        if self.Conference.start_date < timezone.now().date():
            raise ValidationError("La soumission ne peut être faite que pour des conférences à venir.")

        # ✅ 2. Vérifier que les mots-clés ne dépassent pas 10
        if self.keywords:
            keyword_list = [k.strip() for k in self.keywords.split(",") if k.strip()]
            if len(keyword_list) > 10:
                raise ValidationError({"keywords": "Vous ne pouvez pas saisir plus de 10 mots-clés."})

        # ✅ 3. Limiter le nombre de soumissions par utilisateur à 3 par jour
        if self.user_id:
            today = timezone.now().date()
            submissions_today = Submission.objects.filter(
                user=self.user,
                Submission_date__date=today
            ).count()
            if submissions_today >= 3 and not self.pk:  # exclude if updating
                raise ValidationError("Vous ne pouvez pas soumettre plus de 3 conférences par jour.")

    # ✅ Génération automatique de Submission_id
    def save(self, *args, **kwargs):
        if not self.Submission_id:
            random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            self.Submission_id = f"SUB-{random_part}"

        self.full_clean()  # Call validations before saving
        super().save(*args, **kwargs)

