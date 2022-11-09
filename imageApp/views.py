from django.shortcuts import render

def home(request):

    context = {
        'title': 'Remove Background',
        'alert': ''
    }

    return render(request, template_name='image-home.html', context=context)
