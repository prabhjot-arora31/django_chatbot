from django.shortcuts import render

# Create your views here.
def chat(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')