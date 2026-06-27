import re

text = "Python is easy. Python is powerful."

print("search")
print(re.search("Python", text))

print()

print("findall")
print(re.findall("Python", text))

print()

print("split")
print(re.split(r"\s", text))

print()

print("sub")
print(re.sub("Python", "Java", text))

print()

print("match")
print(re.match("Python", text))
