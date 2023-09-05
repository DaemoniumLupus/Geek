# from random import randint


# def find_equal(input_list):
#     count = 0
    
#     unique_list = set(input_list)
   
#     for i in unique_list:
#         count += input_list.count(i)//2
        
        
#     return count


# list1_length = int(input("Введите число элементов первого массива ->"))


# #input_list = [randint(1, 10) for x in range(list1_length)]

# print (input_list := [randint(1, 10) for x in range(list1_length)])
# print (find_equal(input_list))

print(array := [1, 2, 3, 2, 3, 2, 2, 2, 3,3])
print(sum([array.count(x)//2 for x in set(array)]))