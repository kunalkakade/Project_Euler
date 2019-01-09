import time

a = [ i.rstrip() for i in open("pe13").readlines()]
# print(a)
carry = 0
# print(len(a[0]))
i=49
ans = ["0"]*50
while i>=0:
    temp =0
    for j in a:
        temp+=int(j[i])
    print(temp)
    carry +=temp
    print(carry)
    # time.sleep(3)
    if carry > 10:
        carry = carry//10
    ans[i]=str(carry%10)
    print(ans, i)
    print(ans[i] , carry)
    i-=1
print("".join(ans))
