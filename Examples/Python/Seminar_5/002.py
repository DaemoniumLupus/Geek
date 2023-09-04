def sum(a,b):
  if b < 1:
    return a
  return sum(a+1,b-1)

print(sum(2,2))