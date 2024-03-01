from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-home-content/', views.addHomeContent, name='addhomecontent'),
    path('edit-home-content/<str:pk>', views.editHomeContent, name='edithomecontent'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:pk>', views.blogDetail, name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact_form, name='contact'),
    path('view-contacts/', views.view_contacts, name='contacts'),
    path('carrers/', views.carrers, name='carrers'),
    path('carrer/<str:pk>', views.carrersDetail, name='carrer'),
    path('notice/', views.notice, name='notice'),
]
