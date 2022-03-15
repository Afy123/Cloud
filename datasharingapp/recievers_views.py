from django.shortcuts import render, redirect

from datasharingapp.models import Receiver, Upload, Download, Owner


def profile_view_reciever(request):
    u = request.user
    p = Receiver.objects.filter(User=u)
    return render(request, 'Recievers/profile_view_recievers.html', {'profile_view_recievers': p})


def view_file_reciever(request):
    f = Upload.objects.all()
    return render(request, 'Recievers/view_files_recievers.html', {'view_file_recievers': f})


def download_view_reciever(request):
    u = Receiver.objects.get(User=request.user)
    d = Download.objects.filter(Receiver=u)
    return render(request, 'Recievers/download_requests_recievers.html', {'download_view_reciever': d})


def download_request_receiver(request, id):
    upload = Upload.objects.get(id=id)
    r = Receiver.objects.get(User=request.user)
    download = Download.objects.filter(Receiver=r, Upload=upload)
    if download.exists():
        return redirect('download_view_reciever')
    else:
        if request.method == 'POST':
            obj = Download()
            obj.Receiver = r
            obj.Upload = upload
            obj.save()
            return redirect('download_view_reciever')
    return render(request, 'Recievers/download_verify_recievers.html', {'Upload': upload, 'Receiver': r})
