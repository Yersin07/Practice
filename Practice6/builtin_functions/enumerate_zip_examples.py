names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

print("Enumerate:")

for index, name in enumerate(names, start=1):
    print(index, name)

print("\nZip:")

for name, score in zip(names, scores):
    print(name, score)

print("\nSorted:")
print(sorted(scores))

print("\nType conversions:")
print(int("100"))
print(float("25.5"))
print(str(500))
print(list("Python"))

print(type(names))
print(type(scores))
