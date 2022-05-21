from django.forms import ModelForm
from .models import*
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogpostForm(ModelForm):
	class Meta:
		model=blogpost
		fields=['title','content','image','catagory']

		widgets={
		    'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Write your title of blog here'}),
		    'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Write your blog content here'}),
		    'image':forms.FileInput(attrs={'class':'form-control'}),
		    'catagory':forms.Select(attrs={'class':'form-control','placeholder':'Select the catagory'}),
		}


class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']