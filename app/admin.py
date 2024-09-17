from django.contrib import admin

from .models import (
    HeaderText, 
    FooterText,
    Feature,
    About,
    TeamBlock,
    AvatarSocials,
    Courses

)


admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Feature)
admin.site.register(About)
admin.site.register(TeamBlock)
admin.site.register(AvatarSocials)
admin.site.register(Courses)



