from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def select_profile(request):

    return render(
        request,
        'accounts/select_profile.html'
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect('/dashboard/')

    return render(
        request,
        'accounts/login.html'
    )


def hr_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user and user.is_staff:

            login(
                request,
                user
            )

            return redirect('/hr/dashboard/')

    return render(
        request,
        'accounts/hr_login.html'
    )


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        confirm_password = request.POST.get(
            'confirm_password'
        )

        if password != confirm_password:

            return render(
                request,
                'accounts/register.html',
                {
                    'error': 'Passwords do not match'
                }
            )

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                'accounts/register.html',
                {
                    'error': 'Username already exists'
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(
        request,
        'accounts/register.html'
    )

def logout_view(request):

    logout(request)

    return redirect('/')

