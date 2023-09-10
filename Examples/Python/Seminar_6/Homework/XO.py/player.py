class Player:
    symbol = ""

   

    def Enter_turn(self, field: list) -> list:
        while True:
            st = input(f"Enter {self.symbol}(x y): ")
            turn = st.split()
            print(turn)
            if field[int(turn[0]) - 1][int(turn[1]) - 1] == ' ':
                field[int(turn[0]) - 1][int(turn[1]) - 1] = self.symbol
                return field
            else:
                print("Again!")
        
