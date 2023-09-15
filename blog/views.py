from django.shortcuts import render, get_object_or_404
from . import models


def program_lang_view(request):
    lang = models.ProgramLang.objects.all()
    return render(request, 'blog.html', {'lang_key': lang})


