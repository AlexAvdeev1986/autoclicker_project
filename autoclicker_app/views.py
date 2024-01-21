# autoclicker_app/views.py
from django.http import HttpResponse
import pyautogui
import time

def autoclick(request):
    # координаты для клика (замените их на нужные)
    x_coord = 100
    y_coord = 100

    # имитация клика мыши
    pyautogui.click(x=x_coord, y=y_coord)
    
    return HttpResponse("Клик выполнен")
