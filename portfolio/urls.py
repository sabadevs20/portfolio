from django.urls import path
from portfolio import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("projects", views.projects, name="projects"),
    path("blog", views.blog, name="blog"),
]