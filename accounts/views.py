from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login


# Create your views here.

# User signup view, saving user and logging in if valid
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('review_list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
