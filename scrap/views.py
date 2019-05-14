from django.shortcuts import render

# Create your views here.

def scraplist(request):
    return render(request, 'scrap/scraplist.html')