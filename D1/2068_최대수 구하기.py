"""
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
"""
T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    print('#{} {}'.format(test_case, max(li)))

"""
max() 내장함수를 이용하여 최대값 출력
"""