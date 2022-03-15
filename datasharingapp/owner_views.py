import os

from cryptography.fernet import Fernet
from django.shortcuts import render

from datasharingapp.forms import UploadForm
from datasharingapp.models import Owner, Upload, Download


def profile_view_owner(request):
    u = request.user
    p = Owner.objects.filter(User=u)
    return render(request, 'Owners/profile_view_owners.html', {'profile_view': p})


def view_file(request):
    u = request.user
    f = Upload.objects.filter(User=u)
    return render(request, 'Owners/view_files_owner.html', {'view_file': f})


def upload_files(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.User = request.user
            file.Files = request.FILES['Files']
            file_type = file.Files.url.split('.')[-1]
            file_type.lower()
            directory = os.getcwd()
            file_name = directory + file.Files.url
            # for instance in Upload.objects.all():
            #     if instance.Files:
            #         directory = os.getcwd()
            #         file_name = directory+file.Files.url
            file.save()

            class Encryptor():

                def create_key(self):
                    key = Fernet.generate_key()
                    return key

                def write_key(self, key, key_name):
                    with open(key_name, 'wb') as mykey:
                        mykey.write(key)

                def load_key(self, key_name):
                    with open(key_name, 'rb') as mykey:
                        key = mykey.read()
                    return key

                def encrypt_file(self, key, original_file, encrypted_file):
                    f = Fernet(key)

                    with open(original_file, 'rb') as files:
                        original = files.read()

                    encrypted = f.encrypt(original)

                    with open(encrypted_file, 'wb') as files:
                        files.write(encrypted)

                def decrypt_file(self, key, encrypted_file, decrypted_file):
                    f = Fernet(key)

                    with open(encrypted_file, 'rb') as files:
                        encrypted = files.read()

                    decrypted = f.decrypt(encrypted)

                    with open(decrypted_file, 'wb') as files:
                        files.write(decrypted)

            encryptor = Encryptor()

            mykey = encryptor.create_key()

            encryptor.write_key(mykey, 'key.key')

            loaded_key = encryptor.load_key('key.key')

            encryptor.encrypt_file(loaded_key, file_name, file_name + 'enc_')

            encryptor.decrypt_file(loaded_key, file_name + 'enc_', file_name + 'dec_')

            return render(request, 'Owners/confirm_uploaded_owners.html', {'file': file})

    context = {"form": form, }
    return render(request, 'Owners/uploadFile_owners.html', context)


def download_request_owner(request):
    d = Download.objects.all()
    return render(request, 'Owners/download_request_owners.html', {'download_view_owners': d})
