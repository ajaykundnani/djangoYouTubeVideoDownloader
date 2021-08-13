from django.shortcuts import render,HttpResponseRedirect
from pytube import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST['video_name']
        video = YouTube(url)
        stream = video.streams.get_lowest_resolution()
        #stream = video.streams.get_highest_resolution()
        print(stream)
        c = stream.download()
        if c:
            print('Download Successfully')
            return render(request,'index.html',{'stream':stream,'c':c})
    else:
        return render(request,'index.html')

def dowload(request,str):
    url = str
    print(url)
    return render(request,'index.html')