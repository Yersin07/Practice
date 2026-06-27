import shutil
from pathlib import Path

source = Path("../file_handling/sample.txt")
destination = Path("Practice/Data/sample.txt")

destination.parent.mkdir(parents=True, exist_ok=True)

shutil.copy(source, destination)

print("File copied.")

print("\nSearching for .txt files:")

for file in Path("Practice").rglob("*.txt"):
    print(file)
