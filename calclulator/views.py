from django.shortcuts import render
import requests
import json

class DictMapper(dict):
    def __getattr__(self, name):
       if name in self:
           return self[name]
           
    def __setattr__(self, name, value):
       self[name] = value

# Create your views here.
def top(request):
    return render(request, 'top.html')

def select_attacker(request):
    f = open('calclulator/character.json', 'r')
    characters = json.load(f)
    return render(request, 'select_attacker.html', {'characters': characters})

def select_attacked(request):
    f = open('calclulator/character.json', 'r')
    characters = json.load(f)
    chara_list = []
    for character in characters:
        chara = DictMapper(character)
        chara_list.append(chara)
    return render(request, 'select_attacked.html', {'characters': chara_list})

def result(request):
    return render(request, 'result.html')

