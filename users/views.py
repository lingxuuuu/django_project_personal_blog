from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#require a login to access the page
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #if the info that user put in is valid, create user and show success message
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to login!")
            return redirect('login')
    #else return to the page with the register form
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#what is a decorators: it adds function to another functionality: express as @decorator 
#@login_required means that in order to access the profile function, user need to login first
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() 
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')

    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

#http://localhost:8000/login?next=/profile
#the code above means after login, we are expecting the profile page to be next instead of redirecting to home or other ramdom pages.


