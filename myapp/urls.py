from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('booking/',views.booking,name='booking'),

    # artist urls

    path('artist-profile/',views.artist_profile,name='artist-profile'),
    path('artist-dashboard/',views.artist_dashboard,name='artist-dashboard'),
    path('add-photos-video/',views.add_photos_video,name='add-photos-video'),
]