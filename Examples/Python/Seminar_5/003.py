import re




def mul(st: str,q:list,qw):
    pr = re.search("[-+*/]", st)
    list_st = re.split("([-+*/])", st)
    res = ""

    if str(q[qw]) in list_st:
        i = list_st.index(q[qw])
        count = 0
        if len(st) <= 3:
            if q[qw] == '*':
                return int(list_st[0]) * int(list_st[2])
            if q[qw] == '/':
                return int(list_st[0]) / int(list_st[2])
            if q[qw] == '+':
                return int(list_st[0]) + int(list_st[2])
            if q[qw] == '-':
                return int(list_st[0]) - int(list_st[2])
        else:        
            for j in list_st:
                print(res)
                print(0)
                if count == i - 1 and q == "*":
                    res += str(int(list_st[i - 1]) * int(list_st[i + 1]))
                elif count == i - 1 and q == "/":
                    res += str(int(list_st[i - 1]) / int(list_st[i + 1]))
                elif count == i - 1 and q == "+":
                    res += str(int(list_st[i - 1]) + int(list_st[i + 1]))
                elif count == i - 1 and q == "-":
                    res += str(int(list_st[i - 1]) - int(list_st[i + 1]))
                elif count > i - 1 and count <= i + 1:
                    continue
                else:
                    res = str(res) + str(j)
                count += 1
    print(res)
    print(1)
    qw += 1
    if qw > 3:
        return res
    return mul(res,q,qw)


q = ["*", "/", "-", "+"]
qw = 0
num = "1+2*3"
print (mul(num,q,qw))
