from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('about/', views.about, name='about'),

    path('reviews/', views.reviews, name='reviews'),

    path('custom/', views.custom, name='customHome'),

    path('custom/pc/', views.custom_pc, name='customPC'),

    path('custom/device/', views.custom_device, name='customDevice'),

    path('dev/', views.dev, name='devHome'),

    path('web_dev/', views.web_dev, name='webDev'),

    path('bot_dev/', views.bot_dev, name='botDev'),

    path('profile/', views.profile, name='profile'),

    path('feedback/', views.feedback, name='feedback'),

]
