from random import randint


lst = [randint(10, 50) for _ in range(10)]

def hoare_sort(lst):
    if len(lst) > 0:
        x = lst[0]
        left = [i for i in lst if i < x]
        eq = [i for i in lst if i == x]
        right = [i for i in lst if i > x]
        
        lst = hoare_sort(left) + eq + hoare_sort(right)

    return lst

print(hoare_sort(lst))