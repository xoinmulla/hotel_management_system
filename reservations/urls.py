from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('about/', views.about, name='about'),  # About Us page
    path('contact/', views.contact, name='contact'),
    path('manage_reservations/', views.manage_reservations, name='manage_reservations'),

]
