from django.http import HttpResponse
from django.shortcuts import render
import random


def info(request):
    return render(request, "info.html")
    
def students(request,name):
    stu = {
        "김녹형":27,
        "안현상":27,
        "강민지":28
    }
    age = stu.get(name)
    return render(request, "students.html",{"name":name,"age":age})
