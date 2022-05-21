from django.urls import path
from . import views

urlpatterns=[
   path('',views.home,name='home'),
   path('kavdsa/blog',views.blog,name='blog'),
   path('kavdsa/posts',views.post,name='post'),
   path('kavdsa/loginpage',views.loginpage,name='login'),
   path('kavdsa/registerpage',views.register,name='register'),
   path('kavdsa/createblog',views.create,name='createblog'),
   path('kavdsa/updateblog<str:pk>',views.update,name='updateblog'),
   path('kavdsa/deletepost<str:pk>',views.delete,name='deleteblog'),
   path('kavdsa/viewpage<str:pk>',views.viewpage,name='viewpage'),
   path('kavdsa/authors_corner',views.author,name='author'),
   path('kavdsa/aboutpage',views.about,name='about'),
   
]