def power(n):
    if n == 0:
        return 1
    print("power(" + str(n) + ") = 2 * power(" + str(n-1) + ")")
    return 2 * power(n-1)

def power_itr(n):
    print("power(" + str(n) + ") = 1 ")
    output = 1
    for i in range(n):
        print(" * 2")
        output = output*2
    return output

print(power_itr(5))

def add(a, b):
    return a + b
#print(add(1, 2))


def print_add(a, b):
    (a + b)

print(print_add(2, 3))


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

''''def a():
    spam = "a"
    print("HI a")
    print(spam)
    print("BYE a")

def b():
    spam = "b"
    print("HI b")
    a()
    print(spam)
    print("BYE b")

spam = "c"
b()
print(spam)'''''
