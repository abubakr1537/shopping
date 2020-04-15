from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    major = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'students'