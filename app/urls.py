from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('our_teachers/', views.our_teachers, name="our_teachers"),
    path('reviews/', views.reviews, name="reviews"),
   
]
