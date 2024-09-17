from django.db import models
from django.utils import timezone

class HeaderText(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Text"


class FooterText(models.Model):
    text = models.CharField(max_length=255)
        
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"


class Feature(models.Model):
    tag = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Feature"


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    icon = models.CharField(max_length=50, 
        null=True,  
        blank=True, 
        help_text="FontAwesome icon")

    def __str__(self):
        return self.title
   
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"       



class TeamBlock(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="team_blocks")
    social_title = models.CharField(max_length=50, null=True, blank=True)
    social_url = models.URLField(max_length=255, blank=True)
    social_html_class = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Team Block"
        verbose_name_plural = "Team Blocks"
        


class AvatarSocials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"


class Courses(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=250)
    name = models.CharField(max_length=55, null=True, blank=True)
    price = models.CharField(max_length=55)
    image1 = models.ImageField(upload_to="courses", null=True, blank=True)
    image2 = models.ImageField(upload_to="courses", null=True, blank=True)
    icon_data = models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    icon_hours = models.CharField(max_length=50, null=True, blank=True, help_text="FontAwesome icon")
    data = models.CharField(max_length=100, null=True, blank=True)
    duration_in_hours = models.CharField(max_length=10, null=True, blank=True)

 
    def __str__(self):
        return f"{self.title} {self.image1} {self.image2}"

    class Meta:
        verbose_name = "courses"
        verbose_name_plural = "courses"







