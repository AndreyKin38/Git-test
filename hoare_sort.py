from random import randint


lst = [randint(10, 50) for _ in range(10)]

def hoare_sort(lst):
    if len(lst) > 0:
        x = lst[0]
        left = [i for i in lst if i < x]
        eq = [i for i in lst if i == x]
        right = [i for i in lst if i > x]
        
        lst = sort(left) + eq + sort(right)

    return lst

print(sort(lst))