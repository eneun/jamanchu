from django.shortcuts import render, get_object_or_404
from .models import Meeting

# Create your views here.

def listpage(request):
    meetings = Meeting.objects
    return render(request, 'meeting/listpage.html', {'meetings': meetings})

def detail(request, meeting_id):
    meeting_detail = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'meeting/detail.html', {'meeting': meeting_detail})