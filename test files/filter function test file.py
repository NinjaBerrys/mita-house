def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


l = [1, 2, 3, 7, 8, 18, 78, 98, 88]
print(list(filter(greater_than_5, l)))
