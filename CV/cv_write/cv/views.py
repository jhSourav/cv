from django.shortcuts import render
from .models import cv,Career,Education,Programming,Language,projects,personal
# Create your views here.
def image(request):
    title=cv.objects.all()
    career=Career.objects.all()
    edu=Education.objects.all()
    pro=Programming.objects.all()
    lan=Language.objects.all()
    per=personal.objects.all()
    proj=projects.objects.all()

    context={
            'title':title,
            'career':career,
            'edu':edu,
            'program':pro,
            'language':lan,
            'personal':per,
            'projects':proj,
             }
    return render(request, 'base.html',context)


