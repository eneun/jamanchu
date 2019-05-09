from django.shortcuts import render
from meeting.models import Meeting

# Create your views here.
def filters(request):
    return render(request, 'search/filters.html')

def result(request):
    keyword = request.GET['keyword']
    meetings = Meeting.objects.filter(title=keyword)
    return render(request, 'search/result.html', {'meetings': meetings})