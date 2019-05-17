from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from meeting.models import Meeting
from .forms import MessageForm

# Create your views here.
def listmessage(request):
    # 보낸이, 받는이가 본인인 message들만 가져오기
    messages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)
    messages = messages.order_by('-meeting', '-created_at')
    return render(request, 'message/listmessage.html', {'messages': messages})

def show(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    messages = Message.objects.filter(sender=message.sender, receiver=message.receiver) | Message.objects.filter(sender=message.receiver, receiver=message.sender).order_by('-created_at')
    messages = messages.filter(meeting=message.meeting)
    messages = messages.order_by('created_at')
    
    form = MessageForm()
    return render(request, 'message/show.html', {'messages': messages, 'form': form})

def add(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    # 누구와 주고받는 메시지인가를 찾아서 receiver 변수에 저장 
    if message.sender == request.user:
        receiver = message.receiver
    else:
        receiver = message.sender
    meeting = message.meeting

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.meeting = meeting
            message.save()
            # return redirect('listmessge')
            return redirect('showmessage', message_id=message.pk)
        else:
            return HttpResponseRedirect('/')
    else:
        form = MessageForm()
        return redirect('show', message_id=message.pk)

def new(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'message/new.html')

def create(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = meeting.user
            message.meeting = meeting
            message.save()
            return redirect('listmessage')
        # else:
        #     return HttpResponseRedirect('/')
    else:
        form = MessageForm()
        return render(request, 'message/new.html', {'form': form})