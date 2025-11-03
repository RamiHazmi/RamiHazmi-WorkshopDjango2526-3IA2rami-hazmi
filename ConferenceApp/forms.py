from django import forms
from .models import Conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields=['name','theme','location','description','start_date','end_date']
        labels ={
            'name':"titre de la conference",
            'theme':"theme de la conference", 
        }
        widgets= {
            'name' : forms.TextInput(
                attrs= {
                    'placeholder':"entrer un ttitre a la conference"
                }
            ),
            'start_date': forms.DateInput(
                attrs= {
                    'type':"date"
                }
            ),
            'end_date': forms.DateInput(
                attrs= {
                    'type':"date"
                }
            )
        }
