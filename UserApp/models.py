from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def generate_user_id():
    return "USER"+uuid.uuid4().hex[:4].upper()

def verify_email(email):
    domaine=["esprit.tn","seasame.com","tep.tn","central.net"]
    email_domaine=email.split("@")[1]
    if email_domaine not in domaine:
        raise ValidationError("email incorrect")
name_validator = RegexValidator(
    regex='^[a-zA-Z\s-]+$',
    message="ce champ ne doit contenir que des lettres"
)
class User(AbstractUser):
    user_id = models.CharField(max_length=8, unique=True, editable=False)  
    first_name = models.CharField(max_length=250,validators=[name_validator])   
    last_name = models.CharField(max_length=250,validators=[name_validator])
    
    ROLE_CHOICES = [
        ("participant", "Participant"),
        ("committee", "Organizing Committee Member"), 
    ]
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default="participant")
    
    affiliation = models.CharField(max_length=250)
    email = models.EmailField(unique=True,validators=[verify_email])  # better than CharField
    nationality = models.CharField(max_length=250)
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def save(self,*arg,**kwargs):
        if not self.user_id:
            newid=generate_user_id()
            while User.objects.filter(user_id=newid).exists():
                newid=generate_user_id()
            self.user_id=newid
        super().save(*arg,**kwargs)



class OrganizingCommittee(models.Model):
    committee_role = models.CharField(max_length=255, choices=[("chair", "Chair")])
    join_date = models.DateField()
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    user = models.ForeignKey("UserApp.User", on_delete=models.CASCADE, related_name="committees")
    conference = models.ForeignKey("ConferenceApp.Conference", on_delete=models.CASCADE, related_name="committees")

