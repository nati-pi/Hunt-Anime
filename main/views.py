from django.shortcuts import render, redirect
from .models import *


def home(request):
    files = File.objects.all()
    content = request.GET.get('content')
    if content != '' and content is not None:
        files = files.filter(Name__icontains=content)
    context = {
        'queryset': files
    }
    zip(context.values(), context.keys())
    sorted(context)
    zip()

    return render(request, 'index.html', context)
def more(request):
    main = Main.objects.all()
    character = Character.objects.all()
    picture = Picture.objects.all()
    name = request.GET.get('title')
    if name != '' and name is not None:
        main = main.filter(Name__iexact=name)
        picture = picture.filter(title__iexact=name)
        character = character.filter(title__iexact=name)
    context = {'main': main, 'picture': picture, 'character': character}
    return render(request, 'more.html', context)



