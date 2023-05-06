"""
10개의 랜덤한 정수를 입력받아 그 중 홀수인 값만을 더하여 합계를 출력하는 문제.
"""
T = int(input())
for test_case in range(1, T + 1):
    li = map(int, input().split())
    result = 0
    for i in li:
        if i % 2 != 0:
            result += i
    print('#' + str(test_case), str(result))
"""
input값을 리스트로 읽은 후
각각의 요소를 2로 나누어 0으로 떨어지지 않는 값만을
덧셈하고 결과를 출력하는 형식으로 코드 작성
"""