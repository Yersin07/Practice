import os
from pathlib import Path

Path("Practice").mkdir(exist_ok=True)
Path("Practice/Data").mkdir(parents=True, exist_ok=True)
Path("Practice/Images").mkdir(exist_ok=True)

print("Current directory:")
print(os.getcwd())

print("\nFiles and folders:")
for item in os.listdir():
    print(item)
