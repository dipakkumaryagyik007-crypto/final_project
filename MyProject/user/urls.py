from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("home/",views.index),
    path("contact/",views.contact),
    path("gallery/",views.gallery),
    path("wchoose/",views.wchoose),
    path("team/",views.team),
    path("about/",views.about),
    path("placement/",views.placement),
    path("course/",views.course),
    path("facilities/",views.facilities),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
]