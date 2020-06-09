from django.shortcuts import render
from django.http import HttpResponse
import os
from app1.forms import feedbackform
import json
def index(request):
    return render(request, 'index.html')
def videos(request):
    fp=open("data.json")
    data=json.load(fp)
    fp.close()
    urltag,title,desc,thumb=[],[],[],[]
    count=0
    for i in range(len(data["items"])):
        title.append(data["items"][i]['snippet']['title'][:25].lower()+"...")
        desc.append(data["items"][i]['snippet']['description'])
        urltag.append(data["items"][i]['snippet']['resourceId']['videoId'])
        thumb.append(data["items"][i]['snippet']['thumbnails']['medium']['url'])
    count+=len(data['items'])
    fp=open("data1.json")
    data1=json.load(fp)
    fp.close()
    count+=len(data1['items'])
    for i in range(len(data1["items"])):
        title.append(data1["items"][i]['snippet']['title'][:10])
        desc.append(data1["items"][i]['snippet']['description'])
        urltag.append(data1["items"][i]['snippet']['resourceId']['videoId'])
        thumb.append(data1["items"][i]['snippet']['thumbnails']['medium']['url'])

    ls=[]
    for i in range(count):
        dic={'title':title[i],
             'desc':desc[i],
             'tag': urltag[i],
             'thumb':thumb[i]
             }

        ls.append(dic)


    return render(request, 'Videos.html',{'ls':ls})

# return HttpResponse(""+str(title)+"\n\n"+str(desc)+"\n\n"+str(urltag)+"\n\n"+str(thumb))

def apps(request):
    return render(request, 'Apps.html')
def feedbackv(request):
    if request.method == 'POST':
        form = feedbackform(request.POST)

        if form.is_valid():
            pass
        else:
            form = feedbackform()
    return render(request,'feedbackpage.html',{'form': form})