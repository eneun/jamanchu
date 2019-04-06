from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting
# from .forms import MeetingPost

# Create your views here.

def listpage(request):
    meetings = Meeting.objects
    return render(request, 'meeting/listpage.html', {'meetings': meetings})

def detail(request, meeting_id):
    meeting_detail = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'meeting/detail.html', {'meeting': meeting_detail})

def new(request):
    return render(request, 'meeting/new.html')

def create(request):
    meeting = Meeting()
    meeting.title = request.GET['title']
    meeting.body = request.GET['body']
    meeting.date = request.GET['date']
    meeting.start_time = request.GET['start_time']
    meeting.end_time = request.GET['end_time']
    meeting.save()
    return redirect('/meeting/'+str(meeting.id))


# 일반폼 사용시
# def meeting_new(request):
#     if request.method == 'POST':
#         form = MeetingPost(request.POST)

#         if form.is_valid():
#             meeting = Meeting()
#             meeting.category = form.cleaned_data['category']
#             meeting.title = form.cleaned_data['title']
#             meeting.body = form.cleaned_data['body']
#             meeting.save()
#             return redirect('listpage')
#     else:
#         form = MeetingPost()
#     return render(request, 'meeting/new.html', {'form': form})

# 모델폼 사용시
# def meeting_new(request):
#     if request.method == 'POST':
#         form = MeetingPost(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             # post.category = 'hi'
#             post.save()
#             return redirect('listpage')
#     else:
#         form = MeetingPost()
#         return render(request, 'meeting/new.html', {'form': form})