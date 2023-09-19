def pascal_triangle2(a):
    # row = [1]
    # n = [0]
    
    # for i in range(a):
    #     print(row)
    #     row = [x + y for x, y in zip(row + n, n + row)]

    P = []
    for i in range(a):
        row = [1] * (i+1)
        for j in range(len(row)):
            if j != 0 and j != i:
                row[j] = P[i-1][j-1] + P[i-1][j]
        P.append(row)

    return P
        
for row in pascal_triangle2(7):
    print(row)
