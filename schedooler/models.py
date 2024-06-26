from django.db import models


# Create your models here.
class Schedool(models.Model):
    datetime = models.DateTimeField(null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(max_length=500)
    done = models.BooleanField(default=False, null=False)


class Routine(models.Model):
    id = models.BigAutoField()
    routine_rule = models.CharField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



