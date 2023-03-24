from django.urls import path

from . import views

app_name = "shaft"
urlpatterns = [
    path("", views.input, name="input"),
    path("output", views.output, name="output"),
    path("about", views.about, name="about"),
    path('generate_shaft_image/', views.generate_shaft_image, name='generate_shaft_image'),
]
