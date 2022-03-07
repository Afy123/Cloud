from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from datasharingapp.forms import LoginRegister, OwnerRegister, ReceiverRegister
from datasharingapp.models import Owner, Receiver


def homepage_view(request):
    return render(request, 'HomePage/homePage.html')


def authority_view(request):
    return render(request, 'Authority/authority.html')


def owners_view(request):
    u = request.user
    o = Owner.objects.filter(User=u)
    return render(request, 'Owners/owners.html', {'owners_view': o})


def recievers_view(request):
    u = request.user
    r = Receiver.objects.filter(User=u)
    return render(request, 'Recievers/recievers.html', {'recievers_view': r})


def choice_page(request):
    return render(request, 'ChoicePage/choicepage.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('authority')
            elif user.is_owner:
                return redirect('owners')
            elif user.is_receiver:
                return redirect('recievers')
    return render(request, 'Login/loginPage.html')


def owner_register(request):
    login_form = LoginRegister()
    owner_form = OwnerRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        owner_form = OwnerRegister(request.POST)
        if login_form.is_valid() and owner_form.is_valid():
            l = login_form.save(commit=False)
            l.is_owner = True
            l.save()
            o = owner_form.save(commit=False)
            o.User = l
            o.save()
            return redirect('login_view')
    return render(request, 'Owners/registration_owners.html', {'login_form': login_form, 'owner_form': owner_form})


def receiver_register(request):
    login_form = LoginRegister()
    receiver_form = ReceiverRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        receiver_form = ReceiverRegister(request.POST)
        if login_form.is_valid() and receiver_form.is_valid():
            l = login_form.save(commit=False)
            l.is_receiver = True
            l.save()
            r = receiver_form.save(commit=False)
            r.User = l
            r.save()
            return redirect('login_view')
    return render(request, 'Recievers/registration_recievers.html', {'login_form': login_form, 'receiver_form': receiver_form})


def logout_view(request):
    logout(request)
    return redirect('home')
