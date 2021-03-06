"""sns_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", showmain, name="mainpage"),
    path("show/", showhw, name="show"),
    path("introduce/", introduce, name="introduce"),
    path("post/", post, name="post"),
    path("<str:id>", detail, name="detail"),
    path("new/", new, name="new"),
    path("create/", create, name="create"),
    path("edit/<str:id>", edit, name="edit"),
    path("update/<str:id>", update, name="update"),
    path("delete/<str:id>", delete, name="delete"),
    path("<str:post_id>/create_comment", create_comment, name="create_comment"),
    path("edit_comment/<str:id>", edit_comment, name="edit_comment"),
    path("update_comment/<str:id>", update_comment, name="update_comment"),
    path("delete_comment/<str:id>", delete_comment, name="delete_comment"),
    path("like_toggle/<str:post_id>", like_toggle, name="like_toggle"),
    path("dislike_toggle/<str:post_id>", dislike_toggle, name="dislike_toggle"),
]
