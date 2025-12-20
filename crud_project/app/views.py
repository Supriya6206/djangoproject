from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Student

# Create your views here.

def show(request):
    data=Student.objects.filter(isdelete=False)
    return render(request, 'home.html', {'students': data})

def form(request):
    if request.method == "POST":
        data = request.POST
        n= data['name']
        a= data['age']
        c=data['course']
        e=data['email']
        m=data['message']
        
        if int(a)<0 or int(a)>100:
            messages.error(request, "age should not be negative")
            return redirect('form')
    
        var = Student(name=n, age=a, course=c, email=e, message=m)
        var.save()
        messages.success(request, "Data saved successfully")
        return redirect('form')
    return render(request, 'form.html')

def delete_data(request, student_id):
    data=Student.objects.get(id=student_id)
    data.isdelete=True
    data.save()
    return redirect('home')


def recycle(request):
    data= Student.objects.filter(isdelete=True)
    return render(request, 'recycle.html', {'students': data})


def restore(request, student_id):
    data=Student.objects.get(id=student_id)
    data.isdelete=False
    data.save()
    return redirect('home')