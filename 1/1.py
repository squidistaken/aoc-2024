left = []
right = []

pair = input()

while pair != "":
    pair = pair.split("   ")

    left.append(int(pair[0]))
    right.append(int(pair[1]))

    pair = input()

left.sort()
right.sort()

dist = 0
# Both lists have the same length
arr_length = len(left)


for i in range(arr_length):
    dist += abs(left[i] - right[i])

print(dist)
