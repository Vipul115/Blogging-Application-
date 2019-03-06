from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # request.POST contains the data enterd by user into the form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # request.cleaned_data is a dictionary made of all entries made by the user
            message = messages.success(request, f"{username} was registered successfuly")
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

