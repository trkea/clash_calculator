from django.shortcuts import render
import requests
import json
from . import clash_calculator

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
    attacker = request.GET.get('attacker')
    characters = json.load(f)
    chara_list = []
    for character in characters:
        chara = DictMapper(character)
        chara_list.append(chara)
    return render(request, 'select_attacked.html', {'characters': chara_list, 'attacker': attacker})

def result(request):
    clash = clash_calculator.ClashCalculator('calclulator/character.json')
    attacker = clash.load_character(request.GET.get('attacker'))
    defencer = clash.load_character(request.GET.get('defencer'))
    times = clash.calc_damage(attacker, defencer)
    return render(request, 'result.html', {'attacker': attacker, 'defencer': defencer, 'times': times})

