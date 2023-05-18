"""
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]  
    mat_90 = [[0 for _ in range(N)] for _ in range(N)]
    mat_180 = [[0 for _ in range(N)] for _ in range(N)]
    mat_270 = [[0 for _ in range(N)] for _ in range(N)]
    #90도 회전
    for i in range(N):
        for j in range(N):
            mat_90[i][j] = mat[N-1-j][i]
    #180도 회전
    for i in range(N):
        for j in range(N):
            mat_180[i][j] = mat_90[N-1-j][i]
    #270도 회전
    for i in range(N):
        for j in range(N):
            mat_270[i][j] = mat_180[N-1-j][i]
    print('#%d' % tc)
    for i in range(N):
        for a in range(N):
            print(mat_90[i][a], end = '')
        print(end = ' ')
        for b in range(N):
            print(mat_180[i][b], end = '')
        print(end = ' ')
        for c in range(N):
            print(mat_270[i][c], end = '')
        print(end = ' ')
        print()

"""
재검토 필요
"""