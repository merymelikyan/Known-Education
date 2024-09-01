from django.contrib import admin

from .models import (
    HeaderText, 
    FooterText,
    Feature,
    About,
    TeamBlock
)


admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Feature)
admin.site.register(About)
admin.site.register(TeamBlock)

