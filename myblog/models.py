from django.db import models

# Create your models here.
class blogpost(models.Model):
    title=models.CharField(max_length=200,null=True)
    content=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='myblog/img',null=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)

    catagory=(
        ('author','author'),
        ('My_story','My_story'),

        )

    catagory=models.CharField(max_length=200,null=True,choices=catagory)
    
    def __str__(self):
        return self.title
   
    