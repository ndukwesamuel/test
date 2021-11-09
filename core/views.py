from django.shortcuts import render, redirect, reverse
from django.views import generic

# Create your views here.
from core.models import blog
from core.forms import *


# def home(request):
#     blogs = blog.objects.all()
#     context = {
#         'blogs':blogs
#     } 
#     return render(request, 'index.html', context)

# classbase version of home

# class home(generic.TemplateView):
#     template_name = 'index.html'


class home(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset =blog.objects.all()
        return queryset


class blogDetail(generic.DetailView):
    template_name = 'blogdetail.html'
    queryset = blog.objects.all()
    context_object_name = "Detail"




# def createBlog(request):
#     form = BlogForms(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect("core:home")
#         print(form)

#     context = {"form": form}

#     return render(request, 'createblog.html' , context )

class createBlog(generic.CreateView):
    template_name = "createblog.html"
    form_class = BlogForms

    def get_success_url(self):
        return reverse("core:home")

# def updateBlog(request, pk):
#     blogList = blog.objects.get(id=pk)
#     form = BlogForms(request.POST or None, instance=blogList)
#     if form.is_valid():
#         form.save()
#         return redirect("core:home")
#     context = {"form":form}

#     return render(request, "update.html", context)


class updateBlog(generic.UpdateView):
    template_name = "update.html"
    form_class = BlogForms
    queryset = blog.objects.all()

    def get_success_url(self):
        return reverse("core:home")


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


