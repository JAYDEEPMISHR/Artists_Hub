from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('artist-register/',views.artist_register,name='artist-register'),
    path('artist-login/',views.artist_login,name='artist-login'),
    path('artist-home/',views.artist_home,name='artist-home'),
    path('artist-logout/',views.artist_logout,name='artist-logout'),
    path('artist-bio/',views.artist_bio,name='artist-bio'),
    path('artist-change-password/',views.artist_change_password,name='artist-change-password'),
    path('add-image/',views.add_image,name='add-image'),
    ]