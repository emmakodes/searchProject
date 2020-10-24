from django.db import models


class Pet(models.Model):
    image = models.ImageField(upload_to='pet')
    pet_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pet_name

