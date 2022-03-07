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
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)
    Address = models.CharField(max_length=200)
    Files = models.FileField(upload_to="files", unique=True)

    def __str__(self):
        return self.Name


class Complaint(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=200)
    Complaint = models.TextField()
    Date = models.DateField()
    Reply = models.TextField(null=True, blank=True)
