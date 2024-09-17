from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import (
    HeaderText, 
    FooterText,
    Feature,
    About,
    TeamBlock,
    AvatarSocials,
    Courses,
    
)

def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "feature": Feature.objects.all(),
        "about": About.objects.all(),
        "team_blocks": TeamBlock.objects.all(),
        "avatarsocials": AvatarSocials.objects.all(),
        "courses": Courses.objects.all()
        
    }

    return render(request,"base.html", context)
