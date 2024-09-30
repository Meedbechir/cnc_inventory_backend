from django.db import models

class Article(models.Model):
    FAMILLE_CHOICES = [
        ('MI', 'MI'),
        ('MB', 'MB'),
        ('MM', 'MM'),
        ('EM', 'EM'),
    ]

    designation = models.CharField(max_length=255)
    famille = models.CharField(max_length=50, choices=FAMILLE_CHOICES)
    origine = models.CharField(max_length=50)
    quantite = models.IntegerField()
    emplacement = models.CharField(max_length=255, blank=True)
    etat = models.CharField(max_length=50, default='Bon')

    def __str__(self):
        return self.designation
