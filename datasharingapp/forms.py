import os.path

from django import forms
from django.contrib.auth.forms import UserCreationForm

from phonenumber_field.modelfields import PhoneNumberField

from datasharingapp.models import Login, Owner, Receiver, Upload
from datasharingpro import settings


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class OwnerRegister(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('Name', 'Email', 'Address', 'Contact_No')

        def clean_phone(self):
            Contact_No = self.cleaned_data.get("Contact_No")
            z = PhoneNumberField.parse(Contact_No, "IN")
            if not PhoneNumberField.is_valid_number(z):
                raise forms.validationError("Number not in IN format")
            return Contact_No


class ReceiverRegister(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ('Name', 'Email', 'Address', 'Contact_No')

        def clean_phone(self):
            Contact_No = self.cleaned_data.get("Contact_No")
            z = PhoneNumberField.parse(Contact_No, "IN")
            if not PhoneNumberField.is_valid_number(z):
                raise forms.validationError("Number not in IN format")
            return Contact_No


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = [
            'Owner',
            'Title',
            'Description',
            'Files'
        ]

        def clean_file(self):
            Files = self.cleaned_data.get('Files')
            for instance in Upload.objects.all():
                if instance.Files.url == Files.url:
                    raise forms.ValidationError('File already exists :' + Files.url)
            return Files


