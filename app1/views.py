from django.shortcuts import render

# Create your views here.
def google(request):
    return render(request,'google.html')

def flipkart(request):
    return render(request,'flipkart.html')
