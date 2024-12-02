def func(n):
    return lambda a : a*n
    
num = func(2)

print(num(4))
