from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('agency-details/<int:pk>', views.agency, name='agency-details'),
    path('news/', views.news_list, name='news-list'),  # Blog list with pagination
    path('news-details/<int:pk>', views.news_details, name='news-details'),
    path('gallery/', views.gallery_list, name='gallery-list'), 
    path('media/', views.media_list, name='media-list'),

]
