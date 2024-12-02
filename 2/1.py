def is_safe(lvls: list[int]) -> bool:
    current_diff = lvls[1] - lvls[0]

    for i in range(len(lvls) - 1):
        new_diff = lvls[i + 1] - lvls[i]

        if new_diff == 0 or abs(new_diff) > 3 or (new_diff > 0) != (current_diff > 0):
            return False

        current_diff = new_diff

    return True


levels = input()
safe_count = 0

while levels != "":
    levels = list(map(int, levels.split(" ")))
    safe_count += is_safe(levels)

    levels = input()

print(safe_count)
