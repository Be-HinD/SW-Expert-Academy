"""
2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
"""
T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    a, b =divmod(a,b)
    print('#{} {} {}'.format(test_case, a, b))

"""
divmod함수를 이용하여 몫과 나머지를 출력
"""