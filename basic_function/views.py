from django.shortcuts import render, redirect

# Create your views here.


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def index(request):
    return render(request, "index.html")

def add(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if num1.isdigit() or isfloat(num1) and num2.isdigit() or isfloat(num2):
            result = float(num1) +float(num2)
            print(result)
            res = "%.3f" % result
            return render(request, "add.html", {"res":res})
        else:
            res = "Invalid input"
            return render(request, "add.html", {"res":res})
    else:
        return render(request, "add.html")

    
def subract(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if num1.isdigit() or isfloat(num1) and num2.isdigit() or isfloat(num2):
            result = float(num1) - float(num2)
            print(result)
            res = "%.3f" % result
            return render(request, "subtraction.html", {'res':res})
        else:
            res = "Invalid input"
            return render(request, "subtraction.html", {"res":res})
    else:
        return render(request, "subtraction.html")


def multiply(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if num1.isdigit() or isfloat(num1) and num2.isdigit() or isfloat(num2):
            result = float(num1) * float(num2)
            print(result)
            res = "%.3f" % result
            return render(request, "multiplication.html", {'res':res})
        else:
            res = "Invalid input"
            return render(request, "multiplication.html", {"res":res})
    else:
        return render(request, "multiplication.html")


def division(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if num1.isdigit() or isfloat(num1) and num2.isdigit() or isfloat(num2):
            result = float(num1) / float(num2)
            print(result)
            res = "%.3f" % result
            return render(request, "division.html", {'res':res})
        else:
            res = "Invalid input."
            return render(request, "division.html", {"res":res})
    else:
        return render(request, "division.html")