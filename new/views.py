import imp
from django.shortcuts import render,HttpResponse
from datetime import datetime
from new.models import Feedback
from new.models import Care

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def feedback(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        feedback = request.POST.get('feedback')
        feedback = Feedback(fname = fname, lname = lname, username = username, feedback = feedback, date = datetime.today())
        feedback.save()
    return render(request, 'feedback.html')
    # return HttpResponse("feedback")

def solution(request):
    return render(request, 'solution.html')
    #return HttpResponse("solution")

def literature(request):
    return render(request, 'literature_survey.html')
    #return HttpResponse("literature")

def inside(request):
    return render(request, 'inside_ewm.html')
    #return HttpResponse("inside")

def health(request):
    return render(request, 'health_impact.html')
    #return HttpResponse("health")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("about")

def care(request):
    if request.method == "POST":
        first = request.POST.get('first')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        electronic = request.POST.get('electronic')
        items = request.POST.get('items')
        care = Care(first = first, phone = phone, address = address, electronic = electronic, items = items, date = datetime.today())
        care.save()
    return render(request, 'care.html')
    #return HttpResponse("about")
