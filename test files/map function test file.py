def sq(n):
    return n * n


# method 1
l = [1, 2, 4]
l2 = []
for i in l:
    l2.append(sq(i))
print(l2)

# method 2
print(list(map(sq, l)))
