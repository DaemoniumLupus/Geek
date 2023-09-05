from random import randint
from player import Player


class Bot(Player):
    gor = [0, 0, 0]
    vert = [0, 0, 0]
    dia = [0, 0]

    indexis = {}
    

    def Counts(self, field, coord):
        print(f"Counts coord->{coord}")
        self.gor[coord[0]] += 1
        self.vert[coord[1]] += 1
        if coord[0] == coord[1]:
            self.dia[0] += 1
            if coord[0] == coord[1] == 2:
                self.dia[1] += 1
        elif coord[0] == 0 and coord[1] == 3 or coord[0] == 3 and coord[1] == 0:
            self.dia[1] += 1

    def Logic(self, field):
        coord = [0, 0]
        print(field)
        True_symbol = False
        for index,item in enumerate(field):
            if self.symbol in item:
                True_symbol = True
                print(index)
                print(item.index(self.symbol))
                self.indexis = {"index_row":item.index(self.symbol),"index_st":item.index(self.symbol)} 
                 
                

        if True_symbol:
            while True:
                coord = [randint(0, 2), randint(0, 2)]
                self.Counts(field, list(coord))
                if field[coord[0]][coord[1]] == None:
                    field[coord[0]][coord[1]] = self.symbol
                    return field
        else:
            #res = self.gor + self.vert + self.dia
            res = max(set(self.gor + self.vert + self.dia))
            if max(self.gor) == res:
                q = self.gor.index(res)
                print (res)
                buf_st = self.Create_Buffer_String(field,q,0,"gor")
                index_With_Symbol = buf_st.index(self.symbol)
                
                    

    def Enter_turn(self, field) -> list:
        return self.Logic(field)
