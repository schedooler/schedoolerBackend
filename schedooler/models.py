from django.db import models


# Create your models here.
class Schedool(models.Model):
    id = models.BigAutoField()
    datetime = models.DateTimeField()
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(max_length=500)
    done = models.BooleanField(default=False, null=False)


class Routine(models.Model):
    id = models.BigAutoField()
    schedool = models.OneToOneField(Schedool, on_delete=models.DO_NOTHING)
    routine_rule = models.CharField(null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField()



