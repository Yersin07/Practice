from pathlib import Path

file = Path("sample.txt")

with open(file, "w") as f:
    f.write("Alice\n")
    f.write("Bob\n")
    f.write("Charlie\n")

print("File created successfully.")

with open(file, "a") as f:
    f.write("David\n")
    f.write("Emma\n")

print("New lines appended.")
