from random import randint


def random_list(size):
    result = []
    for _ in range(size):
        result.append(randint(-10, 10))
    return result


sp = [-5, 8, -9, 1, 7, 2]

print([x for x in sp])

print([x**2 for x in sp])
print([x**2 if x > 0 else 0 for x in sp ])

print({str(x): x for x in sp})


print({str(i): randint(1,100) for i in range(5)})



#второй список на основе первого если эл-т >0 то возвести в квадрат иначе 0

#print(random_list(10))

#print([randint(1, 100) for _ in range(10)])
