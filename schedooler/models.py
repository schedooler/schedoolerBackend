from django.db import models


# Create your models here.
class Schedool(models.Model):
    datetime = models.DateTimeField(null=False)
    name = models.CharField(max_length=100, null=False)
    content = models.TextField(max_length=500)
    done = models.BooleanField(default=False, null=False)
