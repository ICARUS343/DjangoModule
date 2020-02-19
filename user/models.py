from django.db import models

# Create your models here.


class Authentication(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('Authentication', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

