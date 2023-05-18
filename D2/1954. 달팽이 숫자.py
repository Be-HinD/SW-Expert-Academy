T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [[0 for _ in range(N)] for _ in range(N)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    r = 0
    c = 0
    dist = 0 # 0:우, 1:하, 2:좌, 3:상 --> 0 1 2 3 1
    for i in range(1,N*N+1):
        mat[r][c] = i
        r += dr[dist]
        c += dc[dist]
        if r >= N or c>= N or mat[r][c] != 0 or r<0 or c<0:
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist + 1) % 4
            r += dr[dist]
            c += dc[dist]
    print('#%d' % tc)
    for row in mat:
        print(*row)
            
"""
방향전환하는 방법이 중요.
우측진행 : [고정][++]
좌측진행 : [고정][--]
위로진행 : [--][고정]
밑으로진행 : [++][고정]
또한 진행순서는 우-하-좌-상 고정이기 때문에 진행함과 동시에 유효성체크 후 방향을 바꿔주면서 값을 입력
"""