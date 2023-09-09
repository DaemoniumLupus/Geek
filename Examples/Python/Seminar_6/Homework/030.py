
# def aref(a,d,n):
#   arr = []
#   arr.append(a)
#   for i in range(1,n):
#     arr.append(a+i*d)
#   print(arr)


# a = 1 
# d = 2
# n = 10

# aref(a,d,n)

a = int(input('Enter a: '))
d = int(input('Enter d: '))
n = int(input('Enter n: '))

print(res := [a+i*d for i in range(0,n)])