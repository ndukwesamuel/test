from django.urls import path

from core.views import home, blogDetail,createBlog, updateBlog, blogDelete

app_name = 'core'

urlpatterns = [

    path('', home, name="home"),
    path("createBlog/", createBlog, name="createBlog"),
    path('<str:pk>/', blogDetail, name="blogDetail"), 
    path('<str:pk>/update', updateBlog, name="updateBlog"),
    path('<str:pk>/delete', blogDelete, name="delete")

    
]