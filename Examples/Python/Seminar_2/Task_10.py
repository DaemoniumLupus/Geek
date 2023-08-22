import random


def PositionCoins(position: int):
    count = 0
    for i in coins:
        if i == position:
            count += 1
    return count


def RandPositionCoins(n: int):
    index = 0
    coins = []
    while int(index) < int(n):
        coins.append(random.randint(0, 1))
        index += 1
    return coins



print("Enter the number of coins: ")
n = input()
coins = []
coins = RandPositionCoins(n)

print

position_0 = PositionCoins(0)
position_1 = PositionCoins(1)

if position_0 < position_1:
    print(f'Minimum number of turns: {position_0}')
else: print(f'Minimum number of turns: {position_1}')
