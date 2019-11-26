def tail(iterable, n):
    if n < 1:
        return []
    return list(iterable[-n:])

print(tail([1, 2, 3, 4, 5], 3))
print(tail('hello', 2))
print(tail('hello', 0))
print(tail([1, 2], 0))
squares = (n**2 for n in range(10))
print(tail(squares, 3))
