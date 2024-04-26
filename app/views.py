from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomerRegistrationForm, ExecutorRegistrationForm
from .models import CustomerProfile, ExecutorProfile

def customer_registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            CustomerProfile.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                contact_info=form.cleaned_data['contact_info'],
                experience=form.cleaned_data['experience']
            )
            login(request, user)
            # Перенаправляем пользователя на страницу профиля после регистрации
            return redirect('customer_profile')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'registration/customer_registration.html', {'form': form})

def executor_registration(request):
    if request.method == 'POST':
        form = ExecutorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ExecutorProfile.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                contact_info=form.cleaned_data['contact_info'],
                experience=form.cleaned_data['experience']
            )
            login(request, user)
            # Перенаправляем пользователя на страницу профиля после регистрации
            return redirect('executor_profile')
    else:
        form = ExecutorRegistrationForm()
    return render(request, 'registration/executor_registration.html', {'form': form})

def home(request):
    return render(request, 'home.html')
def customer_profile(request):
    profile = CustomerProfile.objects.get(user=request.user)
    return render(request, 'accounts/customer_profile.html', {'profile': profile})

def executor_profile(request):
    profile = ExecutorProfile.objects.get(user=request.user)
    return render(request, 'accounts/executor_profile.html', {'profile': profile})