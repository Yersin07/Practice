from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map()
square = list(map(lambda x: x * x, numbers))
print("Squares:", square)

# filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# reduce()
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

# Built-in functions
print("Length:", len(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
