def pascal_triangle2(a):
    row = [1]
    n = [0]
    
    for i in range(a):
        print(row)
        row = [x + y for x, y in zip(row + n, n + row)]
        
print(pascal_triangle2(10))
