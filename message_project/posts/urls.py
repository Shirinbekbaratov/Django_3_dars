from django.urls import path
from .views import HomePageView,AboutPage,ContactPage

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPage.as_view(),name='about'),
    path('contact/',ContactPage.as_view(),name='contact'),
]