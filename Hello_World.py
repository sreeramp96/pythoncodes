def print_items(n):
    for i in range(n):  # bigO -> O(n)
        print(i)


def print_items(n):
    for i in range(n):  # O(n)
        print(i)

    for j in range(n):  # O(n)    O(2n)  drop the constant -> O(n)
        print(j)


print_items(10)


def print_items(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)  O(n^2)
            print(i, j)


print_items(10)


def print_items(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            for k in range(n):  # O(n)   O(n^3) => O(n^2)
                print(i, j, k)


print_items(10)


def print_items(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            print(i, j)

    for k in range(n):  # O(n)    O(n^2 + n) drop the constant => O(n^2)
        print(k)


print_items(10)


def add_items(n):
    return n + n + n  # O(1)


def print_items(a, b):
    for i in range(a):
        print(i)

    for i in range(b):  # O(a+b)
        print(i)


def print_items(a, b):
    for i in range(a):
        for i in range(b):  # O(a*b)
            print(i)
