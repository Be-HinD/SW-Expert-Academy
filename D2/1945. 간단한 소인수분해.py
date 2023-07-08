import sys
sys.stdin = open('input.txt', 'r')
def factorization(x):
    d = 2
    while d <= x:
        print(d)
        if x % d == 0:
            result[d] += 1
            x = x / d
        else:
            d = d + 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = {2:0, 3:0, 5:0, 7:0, 11:0}
    factorization(N)
    print('#%d'% tc, end = ' ')
    for value in result.values():
        print(value, end = ' ')
    print()



"""
재귀문제
"""