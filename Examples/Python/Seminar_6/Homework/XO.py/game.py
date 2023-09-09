from tkinter import *
from bot import Bot
from player import Player
import sys
from random import randint

class Game:

  game_field = [[' ']*3 ,[' ']*3,[' ']*3] # игровое поле
  winner = ''


  def __init__(self):
    super().__init__()
    


  def Paint_Game(self):  
    for i in self.game_field:
      print(i)


  def Paint_Choice(self):

    game_true = True
    while game_true:
      print("Select item: ")
      print("1. New Game with bot")
      print("2. New Game")
      print("3. Exit")
      choice = input()
      match int(choice):
        case 1:
          self.Game_Loop(1)
        case 2:
          self.Game_Loop()
        case 3:
          sys.exit()

  def Who_win(self,symbol) -> str:
    stX = [0,0,0]
    stO = [0,0,0]
    rowX = [0,0,0]
    rowO = [0,0,0]
    diaX = [0,0]
    diaO = [0,0]
    for index_st,item_str in enumerate(self.game_field):
      for index_row,element in enumerate(item_str):
        if element != ' ':
          if element == 'X':
            stX[index_st] += 1
            rowX[index_row] += 1
            if index_st == index_row:
              diaX[0] += 1
              if index_st == index_row == 1:
                diaX[1] += 1
            if index_row == 0 and index_st == 2 or index_row == 2 and index_st == 0:
              diaX[1] += 1
          else:
            stO[index_st] += 1
            rowO[index_row] += 1
            if index_st == index_row:
              diaO[0] += 1
              if index_st == index_row == 1:
                diaO[1] += 1
            if index_row == 0 and index_st == 2 or index_row == 2 and index_st == 0:
              diaO[1] += 1
    for i in range(3):
      if stX[i] > 2 or rowX[i] > 2:
        return 'X'
      if stO[i] > 2 or rowO[i] > 2:
        return 'O'
    
    for o,x in diaO,diaX:
      if x > 2:
        return 'X'
      if o > 2:
        return 'O'
    return ''
              

              

  def Game_Loop(self,choice = 0):
    player = [Player(),Player()]
    
    if choice == 1: 
      player[1] = Bot()
    
    if randint(1,100) % 2 == 0:
      player[0].symbol = 'X'
      player[1].symbol = 'O'
      count_game = [0,1,0,1,0,1,0,1,0]
    else:
      player[0].symbol = 'O'
      player[1].symbol = 'X'
      count_game = [1,0,1,0,1,0,1,0,1]

    for i in count_game:
      self.game_field = player[i].Enter_turn(self.game_field)
      self.Paint_Game()
      winner = self.Who_win(player[i].symbol)
      if winner != '':
        if winner == player[0].symbol:
          print("Player win!!!")
          self.game_field = [[' ']*3 ,[' ']*3,[' ']*3]
          break
        else:
          print("Bot win!!!")
          self.game_field = [[' ']*3 ,[' ']*3,[' ']*3]
          break
      
      

      
    
