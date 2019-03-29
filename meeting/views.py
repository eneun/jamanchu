from django.shortcuts import render

# Create your views here.

def listpage(request):
    return render(request, 'meeting/listpage.html')