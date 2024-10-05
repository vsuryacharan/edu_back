# views.py
from django.shortcuts import render
from .assistant import wish, jarvis, takecommand

def home(request):
    # Welcome message when loading the page
    wish()
    return render(request, 'index.html')

def voice_assistant(request):
    # Triggering the voice assistant logic
    query = takecommand().lower()
    jarvis(query)
    return render(request, 'index.html')
