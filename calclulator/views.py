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

def get_url(request):
    return "{0}://{1}".format(request.scheme, request.get_host())

# Create your views here.
def top(request):
    url = get_url(request)
    return render(request, 'top.html', {'url': url})

def select_attacker(request):
    url = get_url(request)
    f = open('calclulator/character.json', 'r')
    characters = json.load(f)
    return render(request, 'select_attacker.html', {'characters': characters, 'url': url})

def select_attacked(request):
    url = get_url(request)
    f = open('calclulator/character.json', 'r')
    attacker = request.GET.get('attacker')
    characters = json.load(f)
    chara_list = []
    for character in characters:
        chara = DictMapper(character)
        chara_list.append(chara)
    return render(request, 'select_attacked.html', {'characters': chara_list, 'attacker': attacker, 'url': url})

def result(request):
    url = get_url(request)
    clash = clash_calculator.ClashCalculator('calclulator/character.json')
    attacker = clash.load_character(request.GET.get('attacker'))
    defencer = clash.load_character(request.GET.get('defencer'))
    times = clash.calc_damage(attacker, defencer)
    return render(request, 'result.html', {'attacker': attacker, 'defencer': defencer, 'times': times, 'url': url})

