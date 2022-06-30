from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


from blog.models import Post
# Create your views here.

def frontpage(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render (request=request, template_name='core/frontpage.html', context={'posts': posts})
    

def aboutpage(request: HttpRequest) -> HttpResponse:
    return render (request=request, template_name='core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

