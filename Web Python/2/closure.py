def counter():
    x = 0
    def increment(y):
        nonlocal x
        x += y
        print(x)
    return increment