def counter():
    x = 0
    def increment(y):
        nonlocal x
        x += y
        print(x)
    return increment

counter1_increment = counter()
counter2_increment = counter()

print counter1_increment(1)
print counter1_increment(7)
print counter1_increment(1)

print '--------------'

print counter2_increment(1)
print counter2_increment(1)