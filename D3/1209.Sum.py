import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []
    #100개 행 합 구하기
    for i in range(100):
        sum_ = 0
        for j in range(100):
            sum_ += arr[i][j]
        result.append(sum_)
    #100개 열 합 구하기
    for i in range(100):
        sum_ = 0
        for j in range(100):
            sum_ += arr[j][i]
        result.append(sum_)
    #대각선 합 구하기
    sum_ = 0
    for i in range(100):
        sum_ += arr[i][i]
    result.append(sum_)
    #대각선 반대 합 구하기
    sum_ = 0
    for i in range(0, 100, -1):
        sum_ += arr[i][i]
    result.append(sum_)
    
    #최종 결과 출력
    print('#{} {}'.format(N, max(result)))

"""
단순 for문 노가다
"""