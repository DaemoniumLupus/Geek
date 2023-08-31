def Search(mas: []) -> {}:
    max = 0
    buf = 0
    res = 0
    for i in range(len(mas)):
        if i == len(mas) - 1:
            buf = mas[i - 1] + mas[i] + mas[0]
        else:
            buf = mas[i - 1] + mas[i] + mas[i + 1]
        if buf > max:
            max = buf
            res = i
            
    return dict.fromkeys([res+1],max)

def Filling(mas: [], num: int) -> []:
    for i in range(num):
        mas.append(int(input(f"Enter the number of berries on the {i+1} bush: ")))
    return mas

a = []
n = int(input("Enter the number of bushes: "))
a = Filling(a,n)
print(Search(a))
