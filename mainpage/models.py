from django.db import models

class AWSAuth(models.Model):
    access_key_id = models.CharField(max_length=80)
    access_secret_key_id = models.CharField(max_length=80)