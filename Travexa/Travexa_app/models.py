from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
