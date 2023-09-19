from random import randint


lst = [randint(10, 50) for _ in range(10)]

def merge_list(lst1, lst2):
    l = []
    
    X = len(lst1)
    Y = len(lst2)

    i = 0
    j = 0
    while i < X and j < Y:
        if lst1[i] <= lst2[j]:
            l.append(lst1[i])
            i += 1
        else:
            l.append(lst2[j])
            j += 1

    l += lst1[i:] + lst2[j:]

    return l

def merge_sort(lst):
    mid = len(lst) // 2
    lst1 = lst[:mid]
    lst2 = lst[mid:]

    if len(lst1) > 1:
        lst1 = merge_sort(lst1)
    if len(lst2) > 1:
        lst2 = merge_sort(lst2)

    return merge_list(lst1, lst2)

print(merge_sort(lst))