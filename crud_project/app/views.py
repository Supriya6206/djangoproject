from django.shortcuts import render

# Create your views here.

def show(request):
    data=Course.objects.all()
    return render(request, 'home.html')