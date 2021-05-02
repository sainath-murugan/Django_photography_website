from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="service"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('gallery/wildlife/', views.wildlife, name="wildlife"),
    path('gallery/products/', views.products, name="products"),
    path('gallery/wedding/', views.wedding, name="wedding"),
    path('gallery/events/', views.events, name="events"),
    path('gallery/modelling/', views.modelling, name="modelling"),
    path('videos/', views.videos, name="videos"),
    path("admins/reset_password/", auth_views.PasswordResetView.as_view()),
    path("admins/reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("admins/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("admins/reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    

]