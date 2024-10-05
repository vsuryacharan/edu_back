# urls.py (inside aiapp)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voice_assistant/', views.voice_assistant, name='voice_assistant'),
]
