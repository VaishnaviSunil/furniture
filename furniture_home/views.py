from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'index.html')

def home(request):
    return render (request,'home.html')

def bed(request):
    return render (request,'bedroom.html')

def living(request):
    return render (request,'livingroom.html')

def about(request):
   return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def accessory(request):
    return render(request,'accessories.html')