import re

text = "python PYTHON Python"

print(re.findall("python", text))
print(re.findall("python", text, re.IGNORECASE))

text2 = """Python
Java
C++
"""

print(re.findall("^Python", text2, re.MULTILINE))
