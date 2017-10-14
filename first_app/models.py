from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=256,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class myUser(models.Model):
    First_name = models.CharField(max_length=256)
    Last_name = models.CharField(max_length=256)
    Email = models.EmailField(max_length=256, unique=True)

    def __str__(self):
        return "{} {}, Email: {}".format(self.First_name,self.Last_name,self.Email)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username