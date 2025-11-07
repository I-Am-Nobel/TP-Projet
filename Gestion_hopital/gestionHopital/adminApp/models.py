from django.db import models

# Create your models here.
class Entreprise(models.Model):
    nom = models.CharField(max_length=45)
    description = models.TextField()
    adresse = models.TextField()
    icone = models.ImageField(uploder_to='entreprise')

class Agent(models.Model):
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)
    phone = models.IntegerField()
    photo = models.ImageField(uploder_to='agent')

class Service(models.Model):
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    icone = models.ImageField(uploder_to='service')
