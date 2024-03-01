from .models import *
from django import forms
from django.forms import ModelForm

class SchoolSetupForm(forms.ModelForm):
    class Meta:
        model = SchoolSetup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SchoolSetupForm, self).__init__(*args, **kwargs)

class SocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SocialsForm, self).__init__(*args, **kwargs)


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)


class VisionForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VisionForm, self).__init__(*args, **kwargs)


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MissionForm, self).__init__(*args, **kwargs)


class MessageFromForm(forms.ModelForm):
    class Meta:
        model = MessageFrom
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MessageFromForm, self).__init__(*args, **kwargs)


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CoursesForm, self).__init__(*args, **kwargs)


class FaqsForm(forms.ModelForm):
    class Meta:
        model = Faqs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FaqsForm, self).__init__(*args, **kwargs)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

class HomeContentForm(forms.ModelForm):
    class Meta:
        model = HomeContent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HomeContentForm, self).__init__(*args, **kwargs)


class PopupMessageForm(forms.ModelForm):
    class Meta:
        model = PopupMessage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PopupMessageForm, self).__init__(*args, **kwargs)


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VacancyForm, self).__init__(*args, **kwargs)
