from django.db import models
from adminApp.models import *

# Create your models here.
class Docteur(models.Model):
    nom= models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    specialite = models.CharField(max_length=50)
    phone = models.IntegerField()
    adresse = models.TextField()
    photo = models.ImageField(uploder_to='docteur')
    addby = models.CharField(max_length=50)

class Patient(models.Model):
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    poids = models.FloatField()
    phone = models.IntegerField()
    taille = models.FloatField()
    photo = models.ImageField(uploder_to='patient')
    addby = models.CharField(max_length=50)


class Maladie(models.Model):
    designation = models.CharField(max_length=50)
    description = models.TextField()
    docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE)
    addby = models.CharField(max_length=50)

class Traitement(models.Model):
    designation = models.CharField(max_length=50)
    medoc = models.CharField(max_length=50)
    maladie = models.ForeignKey(Maladie, on_delete=models.CASCADE)
    addby = models.CharField(max_length=50)

    