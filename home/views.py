from django.shortcuts import render
from .models import *
# Create your views here.
def homeview(request):
    aboutme=about_me.objects.all()
    blogme=blog_me.objects.all()
    contactme=contact_me.objects.all()
    portfoliome=contact_me.objects.all()
    context={
        'me_list': aboutme,
        'blog_list':blogme,
        'contact_list':contactme,
        'portfolio_list':portfoliome,
    }
    return render(request,"index.html",context=context)