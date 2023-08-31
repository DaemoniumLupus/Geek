def Filling(mas: [], num: int, st:str) -> []:
    for i in range(num):
        mas.append(int(input(f"Enter the {i+1} number of the {st} set: ")))
    return mas

def Sort(a:[],b:[]) -> []:
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
    return c

a = []
b = []

n = int(input("Enter the number of elements of the first set: "))
m = int(input("Enter the number of elements of the second set: "))

a = Filling(a, n,'first')
b = Filling(b, m,'second')

print(sorted(set(Sort(a,b))))