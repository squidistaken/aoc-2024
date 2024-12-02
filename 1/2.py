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

similiarity = 0
arr_length = len(left)

right_counter = [0] * 100000

for i in range(arr_length):
    right_counter[right[i]] += 1

for i in range(arr_length):
    similiarity += right_counter[left[i]] * left[i]

print(similiarity)
