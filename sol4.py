def CheckPal(a):
    # print(a)
    a = str(a)
    return a==a[::-1]

ans =0
for i in range(100,999):
    for j in range(100,999):
        if CheckPal(i*j) and i*j > ans :
            ans = i*j
            print(i*j)
print(ans)