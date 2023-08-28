# Требуется найти в массиве list_1 самый близкий
# по величине элемент к заданному числу k
# и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
num = 0
m = k - list_1[0]

for i in list_1:
    if k - i < 0:
        if i - k < m:
            num = i
            m = i - k
    else:
        if k - i < m:
            num = i
            m = k - i    
print(num) 