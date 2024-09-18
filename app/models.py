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
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.text1} {self.text2}"

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
        verbose_name = "AvatarSocial"
        verbose_name_plural = "AvatarSocials"


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



class StudentReviews(models.Model):
    name = models.CharField(max_length=45)
    position = models.CharField(max_length=60)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="studentreviews")
    total_reviews  = models.CharField(max_length=400)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "StudentReview"
        verbose_name_plural = "StudentReviews"



class ContactInfo(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    email_name = models.CharField(max_length=255,blank=True, null=True)
   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ContactInfo"
        verbose_name_plural = "ContactInfo"


class Headquarter(models.Model):
    title = models.CharField(max_length=50)
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Headquarter"
        verbose_name_plural = "Headquarter"


class ContactUst(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="contact_us")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us" 


class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
