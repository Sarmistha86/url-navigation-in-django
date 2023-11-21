from django.shortcuts import render

# Create your views here.
def instagram(request):
    return render(request,'instagram.html')

def facebook(request):
    return render(request,'facebook.html')
