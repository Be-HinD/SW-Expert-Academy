"""
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

주어질 숫자는 30을 넘지 않는다.
"""

T = int(input())
count = 1
for test_case in range(1, T + 2):
    print(count, end = ' ')
    count *= 2

"""
1부터 출력해야하기 때문에 T+2까지 반복
"""