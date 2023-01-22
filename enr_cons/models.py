from django.db import models

class Participant(models.Model):
    nom = models.CharField(max_length=128)
    prenoms = models.CharField(max_length=128)
    tel = models.IntegerField(default=0)
    mail = models.EmailField(max_length=254)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.prenoms})"

