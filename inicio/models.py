from django.db import models

class Club(models.Model):
    deportes = models.CharField(max_length=20)
    edad = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.deportes} {self.edad}'
