def f(x, y):
    if x<y:
        return 0
    if x == y:
        return 1                                                                            
print(f(3, 10) * f(10, 12))
    return f(x+1, y) + f(x+ 2, y)+f(x*2, y)