from pathlib import Path

file = Path("sample.txt")

# read()
with open(file, "r") as f:
    print("Using read():")
    print(f.read())

# readline()
with open(file, "r") as f:
    print("\nUsing readline():")
    print(f.readline())
    print(f.readline())

# readlines()
with open(file, "r") as f:
    print("\nUsing readlines():")
    lines = f.readlines()

for line in lines:
    print(line.strip())
