list = [ 25, 21, 22, 24, 23, 27, 26 ]

for idx in range(1, len(list)):
    j = idx - 1
    next_elem = list[idx]

    while (list[j] > next_elem) and (j >= 0):
        list[j + 1] = list[j]
        j -= 1

    list[j + 1] = next_elem

print(list)