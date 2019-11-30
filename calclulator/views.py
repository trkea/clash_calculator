from django.shortcuts import render
import requests
# Create your views here.
def top(request):
    return render(request, 'top.html')

def select_attacker(request):
    return render(request, 'select_attacker.html')

def select_attacked(request):
    return render(request, 'select_attacked.html')

def result(request):
    return render(request, 'result.html')