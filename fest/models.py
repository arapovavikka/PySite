from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, default="Ivanov")
    phone = models.CharField(max_length=20, default="+7")
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Organizator(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Craftsman(models.Model):
    bio =  models.TextField()
    url = models.CharField(max_length=200)
    image = models.ImageField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.bio

class Country(models.Model):
    name = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.bio

class City(models.Model):
    name = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country)

    def publish(self):
        self.save()

    def __str__(self):
        return self.bio