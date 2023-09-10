from random import randint
from player import Player


class Bot(Player):
    True_symbol = False
    indexis = dict()

    bot_field = [[" "] * 3, [" "] * 3, [" "] * 3]
    player_field = [[" "] * 3, [" "] * 3, [" "] * 3]

    
    

    def Partition(self, field: list):
        for index_str,item_str in enumerate(field):
            for index_element,element in enumerate(item_str):
                if element == self.symbol:
                    self.bot_field[index_str][index_element] = "E"
                    self.player_field[index_str][index_element] =" "
                else:
                    self.bot_field[index_str][index_element] = " "
                    if element != " ":
                        self.player_field[index_str][index_element] ="E"
                    else:
                        self.player_field[index_str][index_element] =" "

    def Diagonaly(self,subfield,field,coord):
        
        if (subfield[1][1] == 'E' and (subfield[0][0] == 'E' or subfield[2][2] == 'E')) or\
               (subfield[0][0] == 'E' and subfield[2][2] == 'E'):
                for i in range(3):
                    if field[i][i] == ' ':
                        coord = [i,i]        
        elif (subfield[1][1] == 'E' and (subfield[0][2] == 'E' or subfield[2][0] == 'E')) or\
            (subfield[0][2] == 'E' and subfield[2][0] == 'E'):
                if field[0][2] == ' ':
                    coord = [0,2]
                if field[2][0] == ' ':
                    coord == [2,0]
                if field[1][1] == ' ':
                    coord = [1][1]
        return coord

    def Work_with_subField(self,field,subField,coord) -> list:
        oponent_st = [0, 0, 0]
        oponent_row = [0, 0, 0]
        for index_st, item_str in enumerate(self.player_field):
                for index_row, element in enumerate(item_str):
                    if element == "E":
                        oponent_st[index_st] += 1
                        oponent_row[index_row] += 1

        for index_st, i in enumerate(oponent_st):
            if i <= 1:
                for index_row, j in enumerate(oponent_row):
                    if j > 1:
                        coord[1] = index_row
                        for index, st in enumerate(field):
                            if st[index_row] == " ":
                                coord[0] = index
            elif i > 1:
                for index_row, j in enumerate(oponent_row):
                    coord[0] = index_st
                    for index, st in enumerate(field):
                        if st[index_row] == " ":
                            coord[0] = index
        return coord


    def Rand_symbol(self, field) -> list:
        coord = [randint(0, 2), randint(0, 2)]
        return coord
        # if field[coord[0]][coord[1]] == ' ':
        #     field[coord[0]][coord[1]] = self.symbol

    def Logic(self, field: list) -> list:
        self.Partition(field)
        coord = [-1, -1]

        if self.True_symbol == False:
            self.True_symbol = True
            while True:
                coord = [randint(0, 2), randint(0, 2)]
                # self.Counts(field, list(coord))
                if field[coord[0]][coord[1]] == " ":
                    break
                               
        else:
            coord = self.Diagonaly(self.bot_field,field,coord)
            if coord[0] == -1 and coord[1] == -1:
                coord = self.Diagonaly(self.player_field,field,coord)
            
            if coord[0] == -1 and coord[1] == -1:  
                coord = self.Work_with_subField(field,self.player_field,coord)
            if coord[0] == -1 and coord[1] == -1:  
                coord = self.Work_with_subField(field,self.bot_field,coord)
                

        
        while coord[0] == -1 and coord[1] == -1 or field[coord[0]][coord[1]] != " ":
            coord = self.Rand_symbol(field)

       
        field[coord[0]][coord[1]] = self.symbol

        return field

    def Enter_turn(self, field) -> list:
        return self.Logic(field)


class test_game:
    game_field = [["O", "X", " "],
                  ["X", "O", " "],
                  [" ", " ", " "]]

    def __init__(self):
        super().__init__()
        self.game_test()

    def game_test(self):
        bot = Bot()
        bot.True_symbol = True
        bot.symbol = "X"
        self.game_field = bot.Enter_turn(self.game_field)
        for i in self.game_field:
            print(i)


# game = test_game()
