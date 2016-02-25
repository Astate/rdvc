from django import forms

from reservation.models import ReservationForm


class ReservationTrueForm(forms.ModelForm):
    """
    A form for suggesting an ice cream flavour. Here we're using a Django ModelForm, but this could
    be as simple or as complex as you like -
    see https://docs.djangoproject.com/en/1.9/topics/forms/
    """
    class Meta:
        model = ReservationForm
        fields = ['demande', 
        'nom', 
        'prenom', 
        'sexe', 
        'cautionnaire', 
        'adresse', 
        'ville', 
        'province', 
        'pays', 
        'codepostal', 
        'numerostel1', 
        'numerostel2', 
        'numerostel3', 
        'numerostel4',
        'email',
        'datenaissance', 
        'appartement', 
        'domaine', 
        'sportetude', 
        'commentaire'
        
        ]
