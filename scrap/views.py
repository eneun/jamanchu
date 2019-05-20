from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Scrap
from meeting.models import Meeting

# Create your views here.

def scraplist(request):
    scraps = Scrap.objects.filter(user = request.user)
    return render(request, 'scrap/scraplist.html', {'scraps': scraps})

def scrap(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    try:
        scrap = Scrap()
        scrap.user = request.user
        scrap.meeting = meeting
        scrap.save()
    except:
        scrap = Scrap.objects.filter(user=request.user)
        scrap = scrap.get(meeting=meeting)
        scrap.delete()
    # return redirect('scraplist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unscrap(request, scrap_id):
    return redirect('scraplist')