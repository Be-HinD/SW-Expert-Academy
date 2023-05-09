"""
1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

단, 주어질 숫자는 10000을 넘지 않는다.
"""

T = int(input())
count = 0
for test_case in range(1, T + 1):
    count += test_case
print(count)

"""
반복문 사용
"""