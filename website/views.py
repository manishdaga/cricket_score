from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def news(request):
    return render(request,'news.html')

def news_desc(request):
    return render(request,'news_desc.html')

def photo(request):
    return render(request,'photo.html')

def score(request):
    return render(request,'score.html')

def team(request):
    return render(request,'team.html')

def video(request):
    return render(request,'video.html')

def live_score(request):
    return render(request,'live_score.html')

def widgets(request):
    return render(request,'widgets.html')