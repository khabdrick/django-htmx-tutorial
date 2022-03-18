from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    def __str__(self):
        return self.name