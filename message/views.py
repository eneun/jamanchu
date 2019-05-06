from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from meeting.models import Meeting
from .forms import MessageForm

# Create your views here.
def listmessage(request):
    # 보낸이, 받는이가 본인인 message들만 가져오기
    messages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)
    return render(request, 'message/listmessage.html', {'messages': messages})

def show(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'message/show.html', {'message': message})

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