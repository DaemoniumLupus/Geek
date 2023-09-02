from Translation import Translation
    
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
