from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .models import *
from .forms import*

# Create your views here.
def register(request):

	form=CreateUserForm()

	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Account has created successfully for'+user)
			return redirect('login')

	context={'form':form}		
	return render(request,'myblog/register.html',context)	

def loginpage(request):
	if request.method=='POST':
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request,username=username,password=password)

			if user is not None:
				login(request,user)
				return redirect('author')
			else:
				pass
				
	else:
		messages.info(request,"username or passsword is incorrect")
				

	return render(request,'myblog/login.html')

def home(request):
	blogs=blogpost.objects.all()[:6]

	context={'blogs':blogs}
	return render(request,'myblog/home.html',context)
	
def viewpage(request,pk):
	blogs=blogpost.objects.get(id=pk)

	context={'blogs':blogs}
	return render(request,'myblog/view.html',context)

def blog(request):
	blogs=blogpost.objects.all()

	context={'blogs':blogs}
	return render(request,'myblog/blog.html',context)

def create(request):
	form=BlogpostForm()

	if request.method=='POST':
		form=BlogpostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('author')

	context={'form':form}
	return render(request,'myblog/create.html',context)		
	
def update(request,pk):
	blogs=blogpost.objects.get(id=pk)
	form=BlogpostForm(instance=blogs)

	if request.method=='POST':
		form=BlogpostForm(request.POST,instance=blogs)
		if form.is_valid():
			form.save()
			return redirect('author')

	context={'form':form}

	return render(request,'myblog/create.html',context)

def delete(request,pk):
	blogs=blogpost.objects.get(id=pk)

	if request.method=='POST':
		blogs.delete()
		return redirect('author')

	context={'blogs':blogs}
	return render(request,'myblog/delete.html',context)	


def post(request):
	blogs=blogpost.objects.all()

	mystory_blogs=blogs.filter(catagory='My_story')

	context={'mystory_blogs':mystory_blogs}
	return render(request,'myblog/post.html',context)

def author(request):
	blogs=blogpost.objects.all()

	context={'blogs':blogs}
	return render(request,'myblog/author.html',context)
	

def about(request):
	blogs=blogpost.objects.all()

	total_blogs=blogs.count()
	authors_blogs=blogs.filter(catagory='author').count()
	mystory_blogs=blogs.filter(catagory='My_story').count()

	context={'total_blogs':total_blogs,'authors_blogs':authors_blogs,'mystory_blogs':mystory_blogs}
	return render(request,'myblog/about.html',context)