from django.db import models

class Club(models.Model):
    deportes = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.deportes} {self.categoria}'
