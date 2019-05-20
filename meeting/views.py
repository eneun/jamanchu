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
    return render(request, 'meeting/new.html')

# 모델폼 사용
def meeting_new(request):
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