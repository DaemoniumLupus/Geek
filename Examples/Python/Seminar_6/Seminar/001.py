from easygui import *
from random import randint


size = int(enterbox("Введите размер"))

msgbox(str({str(i): randint(1,100) for i in range(size)}))