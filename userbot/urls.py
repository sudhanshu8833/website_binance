from django.urls import path
from . import views
app_name = "userbot"
urlpatterns = [
    path("index", views.index, name="index"),
    
]