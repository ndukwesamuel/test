from django.shortcuts import render, redirect, reverse
from django.views import generic

# Create your views here.
from core.models import blog
from core.forms import *


def home(request):

    blogs = blog.objects.all()

    context = {
        'blogs':blogs
    } 

    return render(request, 'index.html', context)


def blogDetail(request, pk):
    Detail = blog.objects.get(id=pk)
    # print(Detail)

    context = {
        "Detail":Detail
    }
    return render(request, "blogdetail.html", context)

def createBlog(request):
    form = BlogForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("core:home")
        print(form)

    context = {"form": form}

    return render(request, 'createblog.html' , context )

def updateBlog(request, pk):
    blogList = blog.objects.get(id=pk)
    form = BlogForms(request.POST or None, instance=blogList)
    if form.is_valid():
        form.save()
        return redirect("core:home")
    context = {"form":form}

    return render(request, "update.html", context)


def blogDelete(request, pk):
    blogList = blog.objects.get(id=pk)
    blogList.delete()
    return redirect("core:home")


class signupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = userform 

    def get_success_url(self):
        return reverse("login")


# class SignupView(generic.CreateView):
#     template_name = "registration/signup.html"
#     form_class = CustomUserCreationForm
#     def get_success_url(self):
#         return reverse("login")


