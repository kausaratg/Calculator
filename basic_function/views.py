from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def add(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']
    if num1.isdigit() and num2.isdigit():
        res = int(num1) + int(num2)
        return render(request, "result.html", {"result":res})
    else:
        res = "Invalid input. Make sure you input only number"
        return render(request, "result.html", {"result":res})
    
