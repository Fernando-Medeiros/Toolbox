import os
from pytube import YouTube
from django.shortcuts import render

from .forms import DownloadVideoForm


def home(request):

    form = DownloadVideoForm()
    
    path = 'static/video'

    context =  {
        'title': 'Video Download',
        'filename': '',
        'thumbnail': '',
        'alert': '',
        'form': form
        }


    if len(os.listdir(path)) >= 1:

        for download in os.listdir(path):
            os.remove('{}/{}'.format(path, download))
        

    if request.method == "POST":
        
        try:
            youtube = YouTube(request.POST['link'])
            print(youtube)
        except:
            context['alert'] = 'LINK INVÁLIDO!'
            

        if context['alert'] == "":

            try:
                request.POST['video']
                filename = youtube.streams.get_highest_resolution().download(output_path=path)
            except:
                filename = youtube.streams.get_audio_only().download(output_path=path)
            

            filename = filename[filename.rindex('/'):]
            context['filename'] = '{}{}'.format(path, filename)
            context['thumbnail'] = youtube.thumbnail_url

        
    return render(request, template_name='home.html', context=context)