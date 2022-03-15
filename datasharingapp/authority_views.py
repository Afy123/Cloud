from django.shortcuts import render, redirect

from datasharingapp.models import Owner, Receiver, Upload, Download


def view_owner(request):
    o = Owner.objects.all()
    return render(request, 'Authority/view_owner.html', {'view_owner': o})


def view_reciever(request):
    r = Receiver.objects.all()
    return render(request, 'Authority/view_reciever.html', {'view_reciever': r})


def view_upload(request):
    u = Upload.objects.all()
    return render(request, 'Authority/view_upload.html', {'view_upload': u})


def view_download_request(request):
    d = Download.objects.all()
    return render(request, 'Authority/view_download.html', {'view_download_request': d})


def confirm_download(request, id):
    a = Download.objects.get(id=id)
    a.Status = 1
    a.save()

    return redirect('view_download_request')


def reject_download(request, id):
    a = Download.objects.get(id=id)
    a.Status = 2
    a.save()
    return redirect('view_download_request')
