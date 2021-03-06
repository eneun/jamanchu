from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfilesForm
from meeting.models import Meeting
from scrap.models import Scrap

# Create your views here.
def mypage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    scraps = Scrap.objects.filter(user=request.user)
    return render(request, 'profiles/mypage.html', {'scraps': scraps})

def new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'profiles/new.html')

def profilecreate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ProfilesForm(request.POST)
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('mypage')
    else:
        form = ProfilesForm()
        return render(request, 'profiles/new.html', {'form': form})

def mymeeting(request):
    if not request.user.is_authenticated:
        return redirect('login')
    meetings = Meeting.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profiles/mymeeting.html', {'meetings': meetings})