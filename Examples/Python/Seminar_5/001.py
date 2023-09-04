def f(a,b):
  if b <=1:
    return a
  return a* f(a,b-1)
  
print(f(3,5))