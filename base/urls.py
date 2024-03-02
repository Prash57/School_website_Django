from django.urls import path
from . import views

urlpatterns = [
    # home page routes
    path('', views.home, name='home'),
    path('view-home-content/', views.viewHomeContent, name='viewhomecontent'),
    path('add-home-content/', views.addHomeContent, name='addhomecontent'),
    path('edit-home-content/<str:pk>', views.editHomeContent, name='edithomecontent'),
    path('delete-home-content/<str:pk>', views.deleteHomeContent, name='deletehomecontent'),

    # school setup routes
    path('school-setup/', views.viewSchool, name='schoolsetup'),
    path('add-school-data/', views.addSchool, name='addschool'),
    path('edit-school-data/<str:pk>', views.editSchool, name='editschool'),
    path('delete-school-data/<str:pk>', views.deleteSchool, name='deleteschool'),

    # social routes
    path('add-social/', views.addSocial, name='addsocial'),
    path('edit-social/<str:pk>', views.editSocial, name='editsocial'),
    path('delete-social/<str:pk>', views.deleteSocial, name='deletesocial'),

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
    path('add-blog/', views.addBlog, name='addblog'),
    path('edit-blog/<str:pk>', views.editBlog, name='editblog'),
    path('delete-blog/<str:pk>', views.deleteBlog, name='deleteblog'),
    path('blog/<str:pk>', views.blogDetail, name='blog'),

    # gallery page routes 
    path('gallery/', views.gallery, name='gallery'),
    path('add-photo/', views.addPhoto, name='addphoto'),
    path('edit-photo/<str:pk>', views.editPhoto, name='editphoto'),
    path('delete-photo/<str:pk>', views.deletePhoto, name='deletephoto'),

    # contact page routes 
    path('contact/', views.contact_form, name='contact'),
    path('view-contacts/', views.view_contacts, name='contacts'),

    # carrers page routes 
    path('carrers/', views.carrers, name='carrers'),
    path('add-vacancy/', views.addVacancy, name='addvacancy'),
    path('edit-vacancy/<str:pk>', views.editVacancy, name='editvacancy'),
    path('delete-vacancy/<str:pk>', views.deleteVacancy, name='deletevacancy'),
    path('carrer/<str:pk>', views.carrersDetail, name='carrer'),

    # notice page routes 
    path('notice/', views.notice, name='notice'),
    path('add-notice/', views.addNotice, name='addnotice'),
    path('edit-notice/<str:pk>', views.editNotice, name='editnotice'),
    path('delete-notice/<str:pk>', views.deleteNotice, name='deletenotice'),

    # popup routes
    path('add-popup-message/', views.addPopupMessage, name='addpopup'),
    path('edit-popup-message/<str:pk>', views.editPopupMessage, name='editpopup'),
    path('delete-popup-message/<str:pk>', views.deletePopupMessage, name='deletepopup'),

    # faqs routes
    path('add-faq/', views.addFaq, name='addfaq'),
    path('edit-faq/<str:pk>', views.editFaq, name='editfaq'),
    path('delete-faq/<str:pk>', views.deleteFaq, name='deletefaq'),

    # courses routes
    path('add-course/', views.addCourse, name='addcourse'),
    path('edit-course/<str:pk>', views.editCourse, name='editcourse'),
    path('delete-course/<str:pk>', views.deleteCourse, name='deletecourse'),

    # testimonials routes
    path('add-testimonial/', views.addTestimonial, name='addtestimonial'),
    path('edit-testimonial/<str:pk>', views.editTestimonial, name='edittestimonial'),
    path('delete-testimonial/<str:pk>', views.deleteTestimonial, name='deletetestimonial'),
    
    # team members routes
    path('add-team-member/', views.addTeamMember, name='addteammember'),
    path('edit-team-member/<str:pk>', views.editTeamMember, name='editteammember'),
    path('delete-team-member/<str:pk>', views.deleteTeamMember, name='deleteteammember'),

    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

]
