from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import (
    HeaderText, 
    FooterText,
    Feature,
    About,
    TeamBlock,
    Courses,
    StudentReviews,
    ContactInfo,
    Headquarter,
    ContactUs,
    Socials,
    QuickLinks
)
 
def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "feature": Feature.objects.all(),
        "about": About.objects.all(),
        "team_blocks": TeamBlock.objects.all(),
        "courses": Courses.objects.all(),
        "studentreviews": StudentReviews.objects.all(),
        "contactinfo": ContactInfo.objects.all().first(),
        "headquarter": Headquarter.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all()
        
    }

    return render(request,"home.html", context)



def about(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "about": About.objects.all(),
        "contactinfo": ContactInfo.objects.all().first(),
        "headquarter": Headquarter.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all()
      
    }
    
    return render(request, "about.html", context)


def contact(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "contactinfo": ContactInfo.objects.all().first(),
        "headquarter": Headquarter.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all()
    }
    return render(request, "contact.html", context)




def courses(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "courses": Courses.objects.all(),
        "contactinfo": ContactInfo.objects.all().first(),
        "headquarter": Headquarter.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all()
      
    }
    
    return render(request, "courses.html", context)


def our_teachers(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "team_blocks": TeamBlock.objects.all(),
        "contactinfo": ContactInfo.objects.all().first(),
        "headquarter": Headquarter.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all()
     
    }
    return render(request, "our_teachers.html", context)




def reviews(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "studentreviews": StudentReviews.objects.all(),
        "contactinfo": ContactInfo.objects.all().first(),
        "headquarter": Headquarter.objects.all().first(),
        "contact_us": ContactUs.objects.all().first(),
        "socials": Socials.objects.all(),
        "quick_links": QuickLinks.objects.all()
      
    }
    
    return render(request, "reviews.html", context)

