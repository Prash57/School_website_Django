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
    return render (request, 'addhomecontent.html', context)

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
    return render(request, 'addhomecontent.html', context)

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