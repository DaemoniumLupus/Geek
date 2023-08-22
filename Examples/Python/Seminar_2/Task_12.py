from math import sqrt

def Answer(s,p):
    D = s*s + 4*p  
    if D > 0:  
        sq = sqrt(D)/2
        p = s/2
        x1 = int(p-sq)
        x2 = int(p+sq)
        return [x1, x2] 


s = int(input('Enter sum: '))
p = -int(input('Enter mul: '))

print(Answer(s,p))

  
 





 