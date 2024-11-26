from django.contrib import admin

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


admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Feature)
admin.site.register(About)
admin.site.register(TeamBlock)
admin.site.register(Courses)
admin.site.register(StudentReviews)
admin.site.register(ContactInfo)
admin.site.register(Headquarter)
admin.site.register(ContactUs)
admin.site.register(Socials)
admin.site.register(QuickLinks)

