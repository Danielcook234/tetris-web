from django.shortcuts import render

def index(request):
    return render(request, 'tetris_game/index.html')

def start_btn(request):
    return render(request, 'tetris_game/game.html',  {'mode': 'single'})

def bot_btn(request):
    return render(request, 'tetris_game/game.html', {'mode':'bot'})