from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':20,'b':3}
    return render(request,'operations.html',d)