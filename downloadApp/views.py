from django.shortcuts import render

# Create your views here.
def home(request):
    context =  {'title': 'Video Download'}
    return render(request, template_name='home.html', context=context)