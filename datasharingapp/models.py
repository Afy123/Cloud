from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Login(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_receiver = models.BooleanField(default=False)


class Owner(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='owner')
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Address = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.Name


class Receiver(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='receiver')
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Address = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.Name


class Upload(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE)
    Owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Files = models.FileField(upload_to="", unique=True)


class Download(models.Model):
    Receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    Upload = models.ForeignKey(Upload, on_delete=models.CASCADE)
    Status = models.IntegerField(default=0)
