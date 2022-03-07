from django.shortcuts import render, redirect

from datasharingapp.forms import UploadForm, ComplaintForm
from datasharingapp.models import Owner, Upload, Complaint


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
            file.save()
            return render(request, 'Owners/confirm_uploaded_owners.html', {'file': file})
    context = {"form": form, }
    return render(request, 'Owners/uploadFile_owners.html', context)


def complaint_view(request):
    u = request.user
    c = Complaint.objects.filter(User=u)
    return render(request, 'Owners/complaint_view_owners.html', {'complaint': c})


def complaint_add(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User = u
            form.save()
            return redirect('complaint_register_owners')
    else:
        return render(request, 'Owners/complaint_register_recievers.html', {'form': form})
