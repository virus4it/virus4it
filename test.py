from random import randint
from time import sleep
from info import *
from help import *

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

            
while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Магазин
''')
    if action == '1':
        fight()
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
        tran(training_type)
    elif action=='3':
        shop()
