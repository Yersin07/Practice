import re

print("===== METACHARACTERS =====")

text = "abc123"

print(re.findall(r".", text))          # .
print(re.findall(r"\d", text))         # digits
print(re.findall(r"\w", text))         # words
print(re.findall(r"\s", "A B C"))      # spaces
print(re.findall(r"\D", text))         # non-digits
print(re.findall(r"\W", "@#$"))        # special symbols
print(re.findall(r"\S", "A B C"))      # non-space

print()

print("===== SETS =====")

print(re.findall(r"[a-z]", text))
print(re.findall(r"[A-Z]", "Python REGEX"))
print(re.findall(r"[0-9]", text))

print()

print("===== QUANTIFIERS =====")

print(re.findall(r"ab*", "ab abb abbb a"))
print(re.findall(r"ab+", "ab abb abbb a"))
print(re.findall(r"ab?", "ab abb a"))
print(re.findall(r"ab{2}", "abb abbb"))
print(re.findall(r"ab{2,3}", "abb abbb abbbb"))

print()

print("===== START END =====")

print(re.search(r"^Python", "Python is easy"))
print(re.search(r"easy$", "Python is easy"))

print()

print("===== GROUPS =====")

text = "My phone is 87071234567"

print(re.findall(r"(\d+)", text))
