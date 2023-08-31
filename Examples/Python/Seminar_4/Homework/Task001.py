import random

k = int(input("Enter K:"))
st = ""
for el in range(k + 1):
    a = random.randrange(-10, 11)
    if k - el > 1 and a != 0:
        st += f"{a:+}x^{k - el}"
    elif k - el == 1 and a != 0:
        st += f"{a:+}x"
    elif a != 0:
        st += f"{a:+}"

if st[0] == '+':
    print (st[1:] + "=0")
else:
    print(st + "=0")
