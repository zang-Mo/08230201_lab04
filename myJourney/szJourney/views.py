from django.shortcuts import render
from .models import Skill, Challenge, Education, Hobby

def index(request):
    skills = Skill.objects.all()
    challenges = Challenge.objects.all()
    education = Education.objects.all()
    return render(request, 'index.html', {
        'skills': skills,
        'challenges': challenges,
        'education': education
    })

def about_me(request):
    hobbies = Hobby.objects.all()
    return render(request, 'aboutMe.html', {'hobbies': hobbies})
