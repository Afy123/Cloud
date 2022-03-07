from django.shortcuts import render

from datasharingapp.models import Owner, Receiver, Upload


def view_owner(request):
    o = Owner.objects.all()
    return render(request, 'Authority/view_owner.html', {'view_owner': o})


def view_reciever(request):
    r = Receiver.objects.all()
    return render(request, 'Authority/view_reciever.html', {'view_reciever': r})


def view_upload(request):
    u = Upload.objects.all()
    return render(request, 'Authority/view_upload.html', {'view_upload': u})
