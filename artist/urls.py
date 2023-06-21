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
    path('artist-add-video/',views.artist_add_video,name='artist-add-video'),
    path('artist-change-profile-pic/',views.artist_change_profile_pic,name='artist-change-profile-pic'),
    ]