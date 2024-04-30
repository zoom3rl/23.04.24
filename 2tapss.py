def f(xx):
    mn = xx[0]
    for i in xx:
        if i > mn:
            mn = i
    return mn

print(f([74,12,45,6,3]))