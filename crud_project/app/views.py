from django.shortcuts import render
from .models import Course

# Create your views here.

def show(request):
    data=Course.objects.all()
    return render(request, 'home.html')

def form(request):
    if request.method == "POST":
        data = request.POST
        n= data['name']
        c=data['course']
        e=data['email']
        m=data['message']
        var = student(name=n, course=c, email=e, message=m)
        var.save()
        messages.success(request, "Data saved successfully")
        return redirect('form')