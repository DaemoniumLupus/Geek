class Player:
  symbol = ''

  def Turn(self,field) -> list:
    return self.Enter_turn(field)
  
  def Enter_turn(self,field:list) -> list:
    while True:
      st = input("Enter x y: ")
      turn = st.split()
      print(turn)
      if field[int(turn[0])][int(turn[1])] == None:
        field[int(turn[0])][int(turn[1])] = self.symbol
        return field
      else:
        print("Again!")
    