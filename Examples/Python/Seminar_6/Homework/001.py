
# def minusfib(n:int) -> int:
#   if (n + 1) % 2 == 0:
#     return fib(n * -1)
#   else:
#     return (-1 * fib(n * -1))

# def fib(n:int) -> int:
#   return mas[n-1] + mas[n-2] 

# mas = []
# minusmas = []
# k = int(input("Enter k: ") )
# for i in range(0,k):
#   if i > 1:
#     mas.append(fib(i))
#     minusmas = [minusfib(-i)] + minusmas
#   elif i == 0:
#     mas.append(0)
#   else:
#     mas.append(1)
#     minusmas.append(1)

# print(minusmas+mas)


def fib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

k = int(input("Enter k:"))
array = [fib(i) for i in range(k)]
array_negafib = [array[i]*-1 if i % 2 == 0 else array[i] for i in range(1, k)]

array_negafib.reverse()
array_negafib.extend(array)

print(array_negafib)