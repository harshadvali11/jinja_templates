from django.shortcuts import render

# Create your views here.

def temp1(request):
    d={'person':'PYTHON','age':25}
    return render(request,'temp1.html',context=d)


def jinjaoperation(request):
    return render(request,'jinjaoperations.html',context={'a':100,'b':200,'c':300})


def forloop(request):
    return render(request,'forloop.html',context={'name':'PYTHON'})