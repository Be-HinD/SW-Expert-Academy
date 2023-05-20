cnt = 0
def pailndrome(x):
    global cnt
    if x == x[::-1]:
        cnt +=1
    
for tc in range(10):
    N = int(input())
    cnt = 0
    array = [list(map(str, input())) for i in range(8)]
    for i in range(8):
        for j in range(8-N + 1):
            pailndrome(array[i][j:j+N])
    for i in range(8):
        for j in range(8-N + 1):
            x = [array[w][i] for w in range(j,j+N)]
            pailndrome(x)
    print(f'#{tc+1} {cnt}')