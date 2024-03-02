from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages

# Create your views here.
# homepage
def home(request):
    context = {}
    if HomeContent.objects.all().exists():
        home_content = HomeContent.objects.filter()[:1].get()
        context = {'home_content': home_content}
    return render (request, 'index.html', context)

# add school setup
def addSchool(request):
    school = SchoolSetup.objects.all()
    form = SchoolSetupForm()
    if request.method == 'POST':
        form = SchoolSetupForm(request.POST, request.FILES)
        if form.is_valid():
            school = form.save(commit=False)
            school.save()

            messages.success(request, 'School setup saved successfully')
            return redirect('home')
    context ={'form': form, 'school': school}
    return render (request, 'base/schoolform.html', context)

# edit school setup
def editSchool(request, pk):
    school = SchoolSetup.objects.get(id=pk)
    form = SchoolSetupForm(instance=school)
    if request.method == 'POST':
        form = SchoolSetupForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            form.save()

            messages.success(request, 'School setup updated successfully')
            return redirect('home')
    context ={'form': form}
    return render (request, 'base/schoolform.html', context)


# delete school setup
def deleteSchool(request, pk):
    school = SchoolSetup.objects.get(id=pk)
    if request.method == 'POST':
        school.delete()

        messages.success(request, 'School setup deleted successfully')
        return redirect('home')
    context ={'obj': school}
    return render (request, 'delete.html', context)


# add social content
def addSocial(request):
    social = Socials.objects.all()
    form = SocialsForm()
    if request.method == 'POST':
        form = SocialsForm(request.POST)
        if form.is_valid():
            social = form.save(commit=False)
            social.save()

            messages.success(request, 'Socials added successfully')
            return redirect('home')
    context = {'social': social, 'form': form}
    return render(request, 'base/socialform.html', context)

# edit social content
def editSocial(request, pk):
    social = Socials.objects.get(id=pk)
    form = SocialsForm(instance=social)
    if request.method == 'POST':
        form = SocialsForm(request.POST, instance=social)
        if form.is_valid():
            form.save()

            messages.success(request, 'Socials updated successfully')
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/socialform.html', context)

# delete social content
def deleteSocial(request, pk):
    social = Socials.objects.get(id=pk)
    if request.method == 'POST':
        social.delete()

        messages.success(request, 'Socials deleted successfully')
        return redirect('home')
    context ={'obj': social}
    return render (request, 'delete.html', context)


# add home content 
def addHomeContent(request):
    home_content = HomeContent.objects.all()
    form = HomeContentForm()
    if request.method == 'POST':
        form = HomeContentForm(request.POST, request.FILES)
        if form.is_valid():
            home_content = form.save(commit=False)
            home_content.save()

            messages.success(request, 'Home content saved successfully')
            return redirect('home')
    context ={'form': form, 'home_content': home_content}
    return render (request, 'base/homecontentform.html', context)

# edit home content 
def editHomeContent(request,pk):
    home_content = HomeContent.objects.get(id=pk)
    form = HomeContentForm(instance=home_content)

    if request.method == 'POST':
        form = HomeContentForm(request.POST, request.FILES, instance=home_content)
        if form.is_valid():
            form.save()

            messages.success(request, 'Home content updated successfully')
            return redirect('home')
        

    context = {'form': form}
    return render(request, 'base/homecontentform.html', context)

# delete home content
def deleteHomeContent(request,pk):
    home_content = HomeContent.objects.get(id=pk)
    if request.method == 'POST':
        home_content.delete()
        
        messages.success(request, 'Home content deleted successfully')
        return redirect('home')
    context = {'obj': home_content}
    return render(request, 'delete.html', context)

# about page
def about(request):
    context = {}
    if About.objects.all().exists():
        about = About.objects.filter()[:1].get()
        context = {'about': about}
    return render (request, 'about.html', context)

# add about section
def addAbout(request):
    about = About.objects.all()
    form = AboutForm()
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            about = form.save(commit=False)
            about.save()

            messages.success(request, "About content saved successfully")
            return redirect('about')
    context = {'about': about, 'form': form}
    return render(request, 'base/aboutform.html', context)

# edit about section
def editAbout(request, pk):
    about = About.objects.get(id=pk)
    form = AboutForm(instance=about)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()

            messages.success(request, "About content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/aboutform.html', context)


# delete about section
def deleteAbout(request,pk):
    about = About.objects.get(id=pk)
    if request.method == 'POST':
        about.delete()
        
        messages.success(request, 'About content deleted successfully')
        return redirect('about')
    context = {'obj': about}
    return render(request, 'delete.html', context)


# add vision section
def addVision(request):
    vision = Vision.objects.all()
    form = VisionForm()
    if request.method == 'POST':
        form = VisionForm(request.POST, request.FILES)
        if form.is_valid():
            vision = form.save(commit=False)
            vision.save()

            messages.success(request, "Vision content saved successfully")
            return redirect('about')
    context = {'vision': vision, 'form': form}
    return render(request, 'base/visionform.html', context)

# edit vision section
def editVision(request, pk):
    vision = Vision.objects.get(id=pk)
    form = VisionForm(instance=vision)
    if request.method == 'POST':
        form = VisionForm(request.POST, request.FILES, instance=vision)
        if form.is_valid():
            form.save()

            messages.success(request, "Vision content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/visionform.html', context)


# delete vision section
def deleteVision(request,pk):
    vision = Vision.objects.get(id=pk)
    if request.method == 'POST':
        vision.delete()
        
        messages.success(request, 'Vision content deleted successfully')
        return redirect('about')
    context = {'obj': vision}
    return render(request, 'delete.html', context)



# add mission section
def addMission(request):
    mission = Mission.objects.all()
    form = MissionForm()
    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.save()

            messages.success(request, "Mission content saved successfully")
            return redirect('about')
    context = {'mission': mission, 'form': form}
    return render(request, 'base/missionform.html', context)

# edit mission section
def editMission(request, pk):
    mission = Mission.objects.get(id=pk)
    form = MissionForm(instance=mission)
    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES, instance=mission)
        if form.is_valid():
            form.save()

            messages.success(request, "Mission content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/missionform.html', context)


# delete mission section
def deleteMission(request,pk):
    mission = Mission.objects.get(id=pk)
    if request.method == 'POST':
        mission.delete()
        
        messages.success(request, 'Mission content deleted successfully')
        return redirect('about')
    context = {'obj': mission}
    return render(request, 'delete.html', context)


# add message from section
def addMessageFrom(request):
    message = MessageFrom.objects.all()
    form = MessageFromForm()
    if request.method == 'POST':
        form = MessageFromForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()

            messages.success(request, "Message From content saved successfully")
            return redirect('about')
    context = {'message': message, 'form': form}
    return render(request, 'base/messagefromform.html', context)

# edit message from section
def editMessageFrom(request, pk):
    message = MessageFrom.objects.get(id=pk)
    form = MessageFromForm(instance=message)
    if request.method == 'POST':
        form = MessageFromForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()

            messages.success(request, "Message From content updated successfully")
            return redirect('about')
    context = {'form': form}
    return render(request, 'base/messagefromform.html', context)


# delete message from section
def deleteMessageFrom(request,pk):
    message = MessageFrom.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        
        messages.success(request, 'Message From content deleted successfully')
        return redirect('home')
    context = {'obj': message}
    return render(request, 'delete.html', context)


# blogs page
def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render (request, 'blogs.html', context)

# add blog
def addBlog(request):
    blog = Blog.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()

            messages.success(request, 'Blog added successfully')
            return redirect('blogs')
    context = {'blog': blog, 'form': form}
    return render(request, 'base/blogform.html', context)


# edit blog
def editBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()

            messages.success(request, 'Blog updated successfully')
            return redirect('blogs')
    context = {'form': form}
    return render(request, 'base/blogform.html', context)

# delete blog
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()

        messages.success(request, 'Blog deleted successfully')
        return redirect('blogs')
    context = {'obj': blog}
    return render(request, 'delete.html', context)

# blogs detail page
def blogDetail(request, pk):
    blogsobj = Blog.objects.get(id=pk)
    context = {'blog': blogsobj}
    return render (request, 'blog_detail.html', context)

# gallery page
def gallery(request):
    photos = Gallery.objects.all()
    context ={'photos': photos}
    return render (request, 'gallery.html', context)

# add photo
def addPhoto(request):
    photo = Gallery.objects.all()
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            messages.success(request, 'Photo added successfully')
            return redirect('gallery')
    context = {'photo': photo, 'form': form}
    return render(request, 'base/photoform.html', context)

# add photo
def editPhoto(request, pk):
    photo = Gallery.objects.get(id=pk)
    form = GalleryForm(instance=photo)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()

            messages.success(request, 'Photo updated successfully')
            return redirect('gallery')
    context = {'form': form}
    return render(request, 'base/photoform.html', context)

# delete photo
def deletePhoto(request, pk):
    photo = Gallery.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()

        messages.success(request, 'Photo deleted successfully')
        return redirect('gallery')
    context = {'obj': photo}
    return render(request, 'base/photoform.html', context)


# contact page
def contact_form(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            messages.success(request, 'Query sent successfully')
            return redirect('contact')

    context ={'form': form, 'contacts': contacts}
    return render(request, 'contact.html', context)

# viewing contacted page
def view_contacts(request):
    contacts = Contact.objects.all()
    context= {'contacts': contacts}
    return render(request, 'view_contacts.html', context)

# carrers/vacancy page
def carrers(request):
    vacancys = Vacancy.objects.all()
    context = {'vacancys': vacancys}
    return render(request, 'carrers.html', context)

# add vacancy
def addVacancy(request):
    vacancy = Vacancy.objects.all()
    form = VacancyForm()
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.save()

            messages.success(request, 'Vacancy added successfully')
            return redirect('carrers')
    context = {'vacancy': vacancy, 'form': form}
    return render(request, 'base/vacancyform.html', context)

# edit vacancy
def editVacancy(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    form = VacancyForm(instance=vacancy)
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES, instance=vacancy)
        if form.is_valid():
            form.save()
 
            messages.success(request, 'Vacancy updated successfully')
            return redirect('carrers')
    context = {'form': form}
    return render(request, 'base/vacancyform.html', context)

# delete vacancy
def deleteVacancy(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    if request.method == 'POST':
        vacancy.delete()

        messages.success(request, 'Vacancy deleted successfully')
        return redirect('carrers')
    context = {'obj': vacancy}
    return render (request, 'delete.html', context)

# carrers/vacancy detail page
def carrersDetail(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    context = {'vacancy': vacancy}
    return render(request, 'carrers_detail.html', context)

# notice page
def notice(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'notice.html', context)

# add notice
def addNotice(request):
    notice = Notice.objects.all()
    form = NoticeForm()
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()

            messages.success(request, 'Notice added successfully')
            return redirect('notice')
    context = {'notice': notice, 'form': form}
    return render(request, 'base/noticeform.html', context)

# edit notice
def editNotice(request, pk):
    notice = Notice.objects.get(id=pk)
    form = NoticeForm(instance=notice)
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()

            messages.success(request, 'Notice updated successfully')
            return redirect('notice')
    context = {'form': form}
    return render(request, 'base/noticeform.html', context)


# delete notice
def deleteNotice(request, pk):
    notice = NoticeForm.objects.get(id=pk)
    if request.method == 'POST':
        notice.delete()
        
        messages.success(request, 'Notice deleted successfully')
        return redirect('home')
    context = {'obj': notice}
    return render(request, 'delete.html', context)


# add popup message
def addPopupMessage(request):
    popup = PopupMessage.objects.all()
    form = PopupMessageForm()
    if request.method == 'POST':
        form = PopupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            popup = form.save(commit=False)
            popup.save()

            messages.success(request, 'Popup Message added successfully')
            return redirect('home') 

    context = {'popup': popup, 'form': form}
    return render (request, 'base/popupform.html', context)

# edit popup message
def editPopupMessage(request, pk):
    popup = PopupMessage.objects.get(id=pk)
    form = PopupMessageForm(instace=popup)
    if request.method == 'POST':
        form = PopupMessageForm(request.POST, request.FILES, instance=popup)
        if form.is_valid():
            form.save()

            messages.success(request, 'Popup Message updated successfully')
            return redirect('home') 

    context = {'form': form}
    return render (request, 'base/popupform.html', context)


# delete popup message
def deletePopupMessage(request, pk):
    popup = PopupMessage.objects.get(id=pk)
    if request.method == 'POST':
        popup.delete()

        messages.success(request, 'Popup Message deleted successfully')
        return redirect('home')
    context = {'obj': popup}
    return render (request, 'delete.html', context)

# add faqs
def addFaq(request):
    faq = Faqs.objects.all()
    form = FaqsForm()
    if request.method =='POST':
        form = FaqsForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()

            messages.success(request, 'Faq added successfully')
            return redirect('home')
    context = {'faq': faq, 'form': form}
    return render (request, 'base/faqform.html', context)


# edit faq
def editFaq(request, pk):
    faq = Faqs.objects.get(id=pk)
    form = FaqsForm(instance=faq)
    if request.method == 'POST':
        form = FaqsForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()

            messages.success(request, 'Faq updated Successfully')
            return redirect('home')
    context = {'form': form}
    return render (request, 'base/faqform.html', context)

# delete faq
def deleteFaq(request, pk):
    faq = Faqs.objects.get(id=pk)
    if request.method == 'POST':
        faq.delete()

        messages.success(request, 'Faq was deleted successfully')
        return redirect('home')
    context= {'obj': faq}
    return render (request, 'delete.html', context)

# add course
def addCourse(request):
    course = Courses.objects.all()
    form = CoursesForm()
    if request.method =='POST':
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()

            messages.success(request, 'Faq added successfully')
            return redirect('home')
    context = {'course': course, 'form': form}
    return render (request, 'base/courseform.html', context)


# edit course
def editCourse(request, pk):
    course = Courses.objects.get(id=pk)
    form = CoursesForm(instance=course)
    if request.method =='POST':
        form = CoursesForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()

            messages.success(request, 'Faq updated successfully')
            return redirect('home')
    context = {'form': form}
    return render (request, 'base/courseform.html', context)


# delete course
def deleteCourse(request, pk):
    course = Courses.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()

        messages.success(request, 'Course was deleted successfully')
        return redirect('home')
    context= {'obj': course}
    return render (request, 'delete.html', context)


# add testimonial
def addTestimonial(request):
    testimonial = Testimonial.objects.all()
    form = TestimonialForm()
    if request.method =='POST':
        testimonial = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()

            messages.success(request, 'Testemonial added successfully')
            return redirect('home')
    context = {'testimonial': testimonial, 'form': form}
    return render (request, 'base/testimonialform.html', context)


# edit testimonial
def editTestimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    form = TestimonialForm(instance=testimonial)
    if request.method =='POST':
        testimonial = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()

            messages.success(request, 'Testemonial added successfully')
            return redirect('home')
    context = {'form': form}
    return render (request, 'base/testimonialform.html', context)



# delete testimonial
def deleteTestimonial(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    if request.method == 'POST':
        testimonial.delete()

        messages.success(request, 'Testimonial was deleted successfully')
        return redirect('home')
    context= {'obj': testimonial}
    return render (request, 'delete.html', context)


# add team member
def addTeamMember(request):
    team = TeamMember.objects.all()
    form = TeamMemberForm()
    if request.method =='POST':
        team = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()

            messages.success(request, 'Team Member added successfully')
            return redirect('about')
    context = {'team': team,'form': form}
    return render (request, 'base/teammemberform.html', context)


# edit team member
def editTeamMember(request, pk):
    team = TeamMember.objects.get(id=pk)
    form = TeamMemberForm(instance=team)
    if request.method =='POST':
        team = TeamMemberForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()

            messages.success(request, 'Team Member updated successfully')
            return redirect('about')
    context = {'form': form}
    return render (request, 'base/teammemberform.html', context)

# delete team member
def deleteTeamMember(request, pk):
    team = TeamMember.objects.get(id=pk)
    if request.method == 'POST':
        team.delete()

        messages.success(request, 'Team Member was deleted successfully')
        return redirect('about')
    context= {'obj': team}
    return render (request, 'delete.html', context)


