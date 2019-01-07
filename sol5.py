'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

end = True
start = 21

def check(a):
    for i in range(1,20):
        if a%i != 0:
            return True
    print(a)
    return False


while check(start):
    start = start+ 1

# 232792560