"""
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!
"""

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    sums = 0
    kils = []
    li = []
    for q in range(N):
        li.append(list(map(int, input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            sums = 0
            for k in range(M):
                for l in range(M):
                    sums += li[i+k][j+l]
            kils.append(sums)
    print('#{} {}'.format(test_case, max(kils)))

"""
N*N의 배열에서 M*M범위 만큼 탐색
4중 for문을 사용하여 각각의 탐색크기를
kils[]에 추가한뒤 max값 리턴
ps. index 1개씩 추가하는 방법을 생각못함, li[0][0] ~ li[1][M]까지 각각의 index를 총합하여 비교
"""