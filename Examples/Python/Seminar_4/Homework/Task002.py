class Translation:
    def Translation(self, num , notation):
        buffer_massive = []
        while num > notation:
            buffer_massive.append(num % notation)
            num //= notation
            
        buffer_massive.append(num%notation)
        if num//notation != 0:
            buffer_massive.append(num//notation)
    
        num_string = ""
        for i in range(1,len(buffer_massive) + 1):
            num_string += str(buffer_massive[-i])
        
        return num_string
    
while True:
    n = input("Enter the number: ")
    try:
        n = int(n)
    except ValueError:
        print("Is not number!")
        continue

    if n < 0:
        print("Enter positive numbers!")
    elif n == 0:
        print("Binary -> 0")
        print("Octal -> 0")
    else:
        print(f"Binary -> {Translation.Translation(Translation,n,2)}")
        print(f"Octal -> {Translation.Translation(Translation,n,8)}")
