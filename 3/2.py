import re

case = input()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

mul_active = True
total = 0

instructions = re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", case)

for i in instructions:
    if i.group(0).startswith("mul"):
        if mul_active:
            x, y = map(int, i.groups())
            total += x * y
    elif i.group(0) == "do()":
        mul_active = True
    elif i.group(0) == "don't()":
        mul_active = False

print(total)
