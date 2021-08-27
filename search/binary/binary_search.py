list = [11, 12, 22, 33, 55, 90, 99]

def binary_search(l, item):
    first = 0
    last = len(list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item: found = True
        else:
            if item < list[midpoint]: last = midpoint - 1
            else: first = midpoint + 1

    return found

print(binary_search(list, 12))
print(binary_search(list, 91))