from django.shortcuts import render, redirect

from datasharingapp.forms import ComplaintForm
from datasharingapp.models import Receiver, Upload, Complaint


def profile_view_reciever(request):
    u = request.user
    p = Receiver.objects.filter(User=u)
    return render(request, 'Recievers/profile_view_recievers.html', {'profile_view_recievers': p})


def view_file_reciever(request):
    f = Upload.objects.all()
    return render(request, 'Recievers/view_files_recievers.html', {'view_file_recievers': f})


def complaint_view_reciever(request):
    u = request.user
    c = Complaint.objects.filter(User=u)
    return render(request, 'Recievers/complaint_view_recievers.html', {'complaint_recievers': c})


def complaint_add_reciever(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User = u
            form.save()
            return redirect('complaint_add_reciever')
    else:
        return render(request, 'Recievers/complaint_register_recievers.html', {'form': form})

