# Create your views here.
import datetime

from django.shortcuts import render, redirect, get_object_or_404

from .form import UserProfileForm
from .models import UserProfile


def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'userprofile/profile_list.html', {'profiles': profiles, 'year': datetime.date.today().year})


def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'userprofile/create_profile.html', {'form': form, 'year': datetime.date.today().year})


def user_detail(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'userprofile/user_detail.html', {'user': user, 'year': datetime.date.today().year})
