from django.db import models


# Create your models here.

class FirstModel(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='images/userProfile/')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.title


