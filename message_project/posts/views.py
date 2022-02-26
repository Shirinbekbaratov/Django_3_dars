from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post
# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name ='home.html'
    context_object_name = 'Barcha_postlar'
class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'