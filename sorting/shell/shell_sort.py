list = [19,2,31,45,30,11,121,27]

def shell_sort(l):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            print("i: " + str(i))
            temp = list[i]
            j = i

            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j -= distance
            list[j] = temp
        distance = distance // 2
    return list

print(shell_sort(list))