from django.urls import path
from . import views

urlpatterns = [
    # home page routes
    path('', views.home, name='home'),
    path('add-home-content/', views.addHomeContent, name='addhomecontent'),
    path('edit-home-content/<str:pk>', views.editHomeContent, name='edithomecontent'),
    path('delete-home-content/<str:pk>', views.deleteHomeContent, name='deletehomecontent'),

    # about page routes 
    path('about/', views.about, name='about'),

    # about page routes for about section
    path('add-about/', views.addAbout, name='addabout'),
    path('edit-about/<str:pk>', views.editAbout, name='editabout'),
    path('delete-about/<str:pk>', views.deleteAbout, name='deleteabout'),

    # about page routes for Vision section
    path('add-vision/', views.addVision, name='addvision'),
    path('edit-vision/<str:pk>', views.editVision, name='editvision'),
    path('delete-vision/<str:pk>', views.deleteVision, name='deletevision'),

    # about page routes for Mission section
    path('add-mission/', views.addMission, name='addmission'),
    path('edit-mission/<str:pk>', views.editMission, name='editmission'),
    path('delete-mission/<str:pk>', views.deleteMission, name='deletemission'),

    # about page routes for Message From section
    path('add-message-from/', views.addMessageFrom, name='addmessagefrom'),
    path('edit-message-from/<str:pk>', views.editMessageFrom, name='editmessagefrom'),
    path('delete-message-form/<str:pk>', views.deleteMessageFrom, name='deletemessagefrom'),

    # blogs page routes 
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:pk>', views.blogDetail, name='blog'),

    # gallery page routes 
    path('gallery/', views.gallery, name='gallery'),

    # contact page routes 
    path('contact/', views.contact_form, name='contact'),
    path('view-contacts/', views.view_contacts, name='contacts'),

    # carrers page routes 
    path('carrers/', views.carrers, name='carrers'),
    path('carrer/<str:pk>', views.carrersDetail, name='carrer'),

    # notice page routes 
    path('notice/', views.notice, name='notice'),
]
