from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})
    
