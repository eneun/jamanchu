from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Meeting
from scrap.models import Scrap
from .forms import MeetingForm

# Create your views here.

def listpage(request):
    meetings = Meeting.objects.order_by('-created_at')
    return render(request, 'meeting/listpage.html', {'meetings': meetings})

def detail(request, meeting_id):
    scrap = Scrap.objects.filter(user=request.user, meeting=meeting_id)
    meeting_detail = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'meeting/detail.html', {'meeting': meeting_detail, 'scrap': scrap})

def new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'meeting/new.html')

# 모델폼 사용
def meeting_new(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.category = 'hi'
            post.user = request.user
            post.save()
            return redirect('listpage')
        # else:
        #     return HttpResponseRedirect('/')
    else:
        form = MeetingForm()
        return render(request, 'meeting/new.html', {'form': form})

def edit(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'meeting/edit.html')

def meeting_update(request, meeting_id):
    if not request.user.is_authenticated:
        return redirect('login')
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', meeting_id=meeting.pk)
    else:
        form = MeetingForm(instance=meeting)
        return render(request, 'meeting/edit.html', {'form': form})

def meeting_destroy(request, meeting_id):
    if not request.user.is_authenticated:
        return redirect('login')
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    meeting.delete()
    return redirect('listpage')