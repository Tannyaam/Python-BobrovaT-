list = [1, 2, 3, 5, 8, 15, 23, 38]
f = lambda i: i ** 2

list_f = [(i, f(i)) for i in list if i % 2 == 0]
print(list_f)