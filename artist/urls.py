from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('artist-register/',views.artist_register,name='artist-register'),
    path('artist-login/',views.artist_login,name='artist-login'),
    path('artist-home/',views.artist_home,name='artist-home'),
    ]