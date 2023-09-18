from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.c


# About Models
class about_me(models.Model):
    ismim =models.CharField(max_length=255,default=True)
    men_kimligim = models.CharField(max_length=255,default=True)
    aboutme_text=RichTextField(default=True)
    region = models.CharField(max_length=255,default=True)
    yoshim=models.IntegerField(default=True)
    email = models.EmailField(max_length=255,default=True)
    image = models.ImageField(default=True)

    def __str__(self):
        return self.ismim


# Blog Models
class blog_me(models.Model):
    title=models.CharField(max_length=50,default=True)
    text = RichTextField(default=True)
    image = models.ImageField(upload_to='images/',default=True)
    datatime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Contact Models
class contact_me(models.Model):
    title = models.CharField(max_length=50,default=True)
    name = models.CharField(max_length=100,default=True)
    telephone = models.CharField(max_length=50,default=True)
    location = models.CharField(max_length=255,default=True)
    email = models.EmailField(default="makhmudx965pa@gmail.com")

    def __str__(self):
        return self.name

# Portfolio Models

class portfolio_me(models.Model):
    title = models.CharField(max_length=50,default=True)
    image = models.ImageField(default=True)
    category = models.FloatField()

    def __str__(self):
        return self.name
