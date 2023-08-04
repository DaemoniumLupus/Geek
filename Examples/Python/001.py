n = 385916
first = n%1000
second = n//1000
res1 = (first%10)+((first//10)%10)+(((first//10)//10)%10)
res2 = (second%10)+((second//10)%10)+(((second//10)//10)%10)
if res1 == res2:
    print("yes")
else:
    print("no")