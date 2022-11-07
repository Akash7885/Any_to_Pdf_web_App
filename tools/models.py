from importlib.metadata import files
from django.db import models

# Create your models here.


class UserFile(models.Model):
    # File_name = models.CharField(max_length=200)
    files = models.FileField(upload_to='')



class UserFeedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    msg = models.TextField(max_length=300)

    def __str__(self):
        return self.name
