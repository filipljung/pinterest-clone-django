from django.urls import path

from .views import *

app_name = 'pinterest'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('about/', about, name='about'),
    path('business/', business, name='business'),
    path('blog/', blog, name='blog'),
]
