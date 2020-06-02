from django.db import models

class ModelEmail(models.Model):
    email = models.CharField(max_length=100, null=True)
