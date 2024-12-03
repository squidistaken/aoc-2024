import re

case = input()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, case)

result = sum(int(x) * int(y) for x, y in matches)

print(result)
