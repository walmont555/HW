def bank(x, y):
    result = 0
    for i in range(y):
        result = x + (x/10)
        x = result
    return round(result, 1)


print(bank(1000, 3))