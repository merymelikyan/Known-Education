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
        
    def __str__(self):
        return self.title
   

        #return f"{self.title} {self.description}"

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"       



class TeamBlock(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="team_blocks")

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Team Block"
        verbose_name_plural = "Team Blocks"
        