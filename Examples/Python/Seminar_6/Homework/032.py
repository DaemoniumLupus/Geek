from random import randint

min = 15
max = 25 
s = [randint(0,100)for i  in range(20)]
res = []
print(res := [s.index(i) for i in s if i > min and i < max])
