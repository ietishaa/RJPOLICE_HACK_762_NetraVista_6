from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('index', views.index, name='index'),
    # path("about", views.about, name="about"),
    path("add_camera", views.add_camera, name="add_camera"),
    path("signup", views.signup, name="signup"),
    # path("signin", views.signin, name="signin"),
]