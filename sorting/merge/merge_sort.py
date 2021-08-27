list = [44, 16, 83, 7, 67, 21, 34, 45, 10]

def merge_sort(l):
    if len(l) <= 1: return l

    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]

    merge_sort(left)
    merge_sort(right)

    a = 0
    b = 0
    c = 0

    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            l[c] = left[a]
            a += 1
        else:
            l[c] = right[b]
            b += 1
        c += 1
    
    while a < len(left):
        l[c] = left[a]
        a += 1
        c += 1

    while b < len(right):
        l[c] = right[b]
        b += 1
        c += 1
    return l

print(merge_sort(list))
