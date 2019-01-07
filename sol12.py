def count_divisers(n):
    div = []
    for i in range(1,int(n/2)):
        if n % i == 0:
            div.append(i)
            div.append(n/i)
    div = list(set(div))
    # print(div)
    print(n,div.__len__())
    if div.__len__() > 500:
        return False
    else:
        return True

if __name__ == '__main__':

    n=1
    s = 0
    while count_divisers(s):
        s = (n*(n+1))/2
        n+=1
        print(s)
    # count_divisers(28)
    print("FINAl")
    print(s)


