import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0
    s, e = N//2, N//2
    for i in range(N):
        for j in range(s, e +1):
            result += arr[i][j]
            
        if i < N//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print('#{} {}'.format(tc, result))

"""
구현문제 / 첫번째 열부터 홀수(1,3,5....)만큼 인덱스를 어떻게 가져올지 생각해야하는 문제
"""