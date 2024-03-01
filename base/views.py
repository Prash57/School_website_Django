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

# about page
def about(request):
    context = {}
    if About.objects.all().exists():
        about = About.objects.filter()[:1].get()
        context = {'about': about}
    return render (request, 'about.html', context)

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