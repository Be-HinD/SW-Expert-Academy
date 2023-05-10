"""
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
"""

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    li = [[0] * n for _ in range(n)]
    li[0][0] = 1
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                li[i][j] = 1
            else:
                li[i][j] = li[i-1][j-1] + li[i-1][j]
    print('#%d' % test_case)
    for k in range(n):
        for l in range(n):
            if li[k][l]:
                print(li[k][l], end = ' ')
        print()

"""
입력크기 N만큼의 리스트를 생성
li[0][0]에 초기값 1을 할당 후
li[1][n] ~ li[n][n] 까지 이전 리스트의 값을
비교하여 값을 넣어주고 결과값 출력
"""