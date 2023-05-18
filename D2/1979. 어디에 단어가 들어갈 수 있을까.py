"""
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
"""

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puz = []
    result = 0
    sum_ = 0
    for i in range(N):
        line = list(map(int, input().split()))
        puz.append(line)
    for i in range(N):
        sum_ = 0
        for j in range(N):
            if puz[i][j] == 1:
                sum_ += 1
                if j+1 < N:
                    if sum_ == K and puz[i][j+1] == 0:
                        result += 1
                        sum_ = 0
                elif sum_ == K:
                    result += 1
                    sum_ = 0
            else:
                sum_ = 0
    for i in range(N):
        sum_ = 0
        for j in range(N):
            if puz[j][i] == 1:
                sum_ += 1
                if j+1 < N:
                    if sum_ == K and puz[j+1][i] == 0:
                        result += 1
                        sum_ = 0
                elif sum_ == K:
                    result += 1
                    sum_ = 0
            else:
                sum_ = 0
    print('#{} {}'.format(test_case, result))

"""
주어진 Input을 리스트에 담고, 가로와 세로순으로 sum_을 체크하면서 들어갈 수 있는 공간값인 result를 증감    
"""