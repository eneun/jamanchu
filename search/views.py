from django.shortcuts import render
from meeting.models import Meeting
from datetime import datetime
from datetime import time

# Create your views here.
def filters(request):
    return render(request, 'search/filters.html')

def result(request):
    keyword = request.GET['keyword']
    stime=request.GET['stime']
    etime=request.GET['etime']
    cat=request.GET['cate']
    search_date=request.GET['date']
    meetings = Meeting.objects.all()
    if keyword:
        meetings = Meeting.objects.filter(title__icontains=keyword)
    if cat:
        if cat=='meal':
             meetings = Meeting.objects.filter(category='식사')
        elif cat=='culture':
             meetings = Meeting.objects.filter(category='문화')
        elif cat=='sports':
             meetings = Meeting.objects.filter(category='스포츠/레저')
        elif cat=='hobby':
             meetings = Meeting.objects.filter(category='취미/힐링')
        elif cat=='study':
             meetings = Meeting.objects.filter(category='스터디')
        elif cat=='etc':
             meetings = Meeting.objects.filter(category='기타')
    if search_date:
        meetings = Meeting.objects.filter(date = search_date)
    if stime and etime:
        meetings = Meeting.objects.filter(start_time__range=[stime,etime])
        meetings = Meeting.objects.filter(end_time__range=[stime,etime])
    elif etime:
       meetings = Meeting.objects.filter(end_time__range=[time(0,0),etime])
    elif stime:
        meetings = Meeting.objects.filter(start_time__range=[stime,time(23,59)])
    return render(request, 'search/result.html', {'meetings': meetings})
