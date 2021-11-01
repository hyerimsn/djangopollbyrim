from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    if request.GET:
        user=User()
        user.save()
        return redirect('quiz', user.pk)
    return render(request, 'home.html')


def quiz(request):
    return render(request, 'quiz.html')