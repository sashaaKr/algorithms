list = [ 25, 21, 22, 24, 23, 27, 26 ]
lastIndex = len(list) - 1

for passNo in range(lastIndex, 0, -1):
    print('passNo: ' + str(passNo))
    for idx in range(passNo):
        print('index: ' + str(idx))
        if list[idx] > list[idx + 1]:
            list[idx], list[idx + 1] = list[idx + 1], list[idx]

print(list)