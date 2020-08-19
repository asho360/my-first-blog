from django import forms
from .models import Post, CV, Experience

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text', )

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('name', 'address', 'number', 'email', 'bio')


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('title', 'company', 'description', 'start_date', 'end_date')
