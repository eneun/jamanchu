from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Scrap
from meeting.models import Meeting

# Create your views here.

def scraplist(request):
    if not request.user.is_authenticated:
        return redirect('login')
    scraps = Scrap.objects.filter(user = request.user)
    return render(request, 'scrap/scraplist.html', {'scraps': scraps})

def scrap(request, meeting_id):
    if not request.user.is_authenticated:
        return redirect('login')
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    check = Scrap.objects.filter(user=request.user, meeting=meeting)
    if not check:
        scrap = Scrap()
        scrap.user = request.user
        scrap.meeting = meeting
        scrap.save()
    else:
        scrap = Scrap.objects.filter(user=request.user, meeting=meeting)
        scrap.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))