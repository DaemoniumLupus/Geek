from tkinter import *
from bot import Bot
from player import Player
import sys
from random import randint

class Game:

  game_field = [[None]*3 ,[None]*3,[None]*3] # игровое поле
  winner = ''
  def __init__(self):
    super().__init__()
    


  def Paint_Game(self,field):
    for i in field:
      print (i)


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

  def Who_win(self,field) -> str:
    pass

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
      
      winner = self.Who_win(self.game_field)
      self.Paint_Game(self.game_field)
      

      
    
