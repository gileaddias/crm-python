from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile

# Create your views here.
def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()
            Userprofile.objects.create(user=user)

            return redirect('/login/')
        
    else:

        form = UserCreationForm()

    form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {

        'form' : form
        
    })  
          