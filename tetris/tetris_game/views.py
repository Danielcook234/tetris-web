from django.shortcuts import render

def index(request):
    return render(request, 'tetris_game/index.html')