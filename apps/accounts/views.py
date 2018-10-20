from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def dashboard(request):
    content = "Welkommen!!!"
    return render(request, "accounts/dashboard.html", {"content":content} )

def dashboard_logout(request):
    content = "You have been logged out"
    return render(request, "accounts/logout_page.html", {"content":content} )

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register_page.html', {'form': form})


def login_page(request):

    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     if user.is_active:
    #         login(request, user)
    #         # Redirect to a success page.
    #     else:
    #         # Return a 'disabled account' error message
    # else:
    #     # Return an 'invalid login' error message.

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # find the user from the DB
            user = form.get_user()
            # log user in
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:dashboard')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login_page.html', {'form':form})
    # return render(request, 'accounts/login_page.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:dashboard_logout')
