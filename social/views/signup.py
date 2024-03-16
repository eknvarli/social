from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from social.forms import SignupForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                form.save()
                user = authenticate(username=username, password=password)
                login(request, user)

                return redirect('index')
        else:
            form = SignupForm()

        return render(request, 'social/signup.jinja', context={
            'form':form,
        })