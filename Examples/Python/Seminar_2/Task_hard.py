
def Number_Int(num: int):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

def Number_Float(num: float):
    count = 0
    if num < 1:
        count = 1
        
    while num % 1 != 0:
        num *= 10
    return Number_Int(num) + count



num = str(input("Enter number: "))

true_int = True

for i in num:
    if i == '.' or i == ',':
        true_int = False
        break
    
if true_int and int(num) == 0:
    print(1)
elif true_int:
    print(Number_Int(int(num)))
else:
    print(Number_Float(float(num)))
    


    