from django.db import models

from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

SEXE_CHOICES = (
    ('H', 'Homme'),
    ('F', 'Femme'),
)

APPARTEMENT_CHOICES = (
    ('M', 'Mixte'),
    ('NM', 'Non-Mixte'),
)

DEMANDE_CHOICES = (
    ('JAN', 'Ma demande est pour la session commençant en janvier prochain'),
    ('AOU1', 'Le Cégep Garneau est mon premier choix de cégep et ma demande de réservation de chambre est conditionnel à mon acceptation au premier tour d\'admission pour l\'année scolaire qui commence en août prochain.'),
    ('AOU2', 'Le Cégep Garneau est mon premier choix de cégep et ma demande de réservation de chambre est pour le deuxième tour d\'admission pour l\'année scolaire qui commence en août prochain.'),
    ('AOU3', 'Le Cégep Garneau est mon premier choix de cégep et ma demande de réservation de chambre est pour le troisième tour d\'admission pour l\'année scolaire qui commence en août prochain.'),
    ('COM1', 'Le Cégep Garneau n\'est pas mon premier choix (Inscrire les précisions dans la section commentaires)'),
    ('COM2', 'Autre (Inscrire les précisions dans la section commentaires)'),
)

SPORT_CHOICES = (
    (' ', 'Aucun'),
    ('ba', 'Badminton'),
    ('bb', 'BasketBall'),
    ('cl', 'Cheerleading'),
    ('cc', 'CrossCountry'),
    ('fb', 'FootBall'),
    ('ru', 'Rugby'),
    ('so', 'Soccer'),
    ('vb', 'VolleyBall'),
)

PROVINCE_CHOICES = (('AB', 'Alberta'), ('BC', 'Colombie-Britanique'), ('MB', 'Manitoba'), ('NB', 'Nouveau-Brunswick'), ('NL', 'Terre-Neuve-et-Labrador'), ('NT', 'Territoires du Nord-Ouest'), ('NS', 'Nouvelle-Écosse'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Île-du-Prince-Édouard'), ('QC', 'Québec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon'))


class ReservationForm(models.Model):
    demande = models.CharField(max_length=200, choices=DEMANDE_CHOICES)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sexe = models.CharField(max_length=4, choices=SEXE_CHOICES)
    cautionnaire = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    province = models.CharField(max_length=200, choices=PROVINCE_CHOICES)
    pays = models.CharField(max_length=200)
    codepostal = models.CharField(max_length=7)
    numerostel1 = models.CharField(max_length=14)
    numerostel2 = models.CharField(max_length=14)
    numerostel3 = models.CharField(max_length=14)
    numerostel4 = models.CharField(max_length=14)
    email = models.EmailField()
    datenaissance = models.DateField()
    appartement = models.CharField(max_length=200, choices=APPARTEMENT_CHOICES)
    domaine = models.CharField(max_length=200)
    sportetude = models.CharField(max_length=20, choices=SPORT_CHOICES)
    commentaire = models.TextField(max_length=2500)
    
class ReservationFormPage(Page):
    intro = RichTextField(blank=True)
    confirmation_page_title = models.CharField(max_length=255, help_text="Texte pour le titre de la page merci")
    
    content_panels = Page.content_panels + [
        FieldPanel('intro',  classname="full"), 
        FieldPanel('confirmation_page_title'), 
    ]
    
    def serve(self, request):
        from reservation.forms import ReservationTrueForm

        if request.method == 'POST':
            form = ReservationTrueForm(request.POST)
            if form.is_valid():
                reserv = form.save()
                return render(request, 'reservation/confirmation.html', {
                    'page': self,
                    'reserv': reserv,
                })
        else:
            form = ReservationTrueForm()

        return render(request, 'reservation/reservation.html', {
            'page': self,
            'form': form,
        })
