import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mylist = []
    for i in range(N):
        mylist.append(list(map(int, input().split())))
    result_x = []
    result_plus = []
    # (0,0) 부터 (N,N)까지 이동하면서 퇴치값 저장
    for i in range(N):
        for j in range(N):
            result = 0
            
            #M = 3일경우 #N = 2
            for p in range(j-M+1, j+M, 1): #result_plus 값 찾기
                try:
                    if 0<=p<N:
                        result += mylist[i][p]#x축
                except:
                    pass
            for p in range(i-M+1, i+M, 1): # 
                try:
                    if 0<=p<N:
                        result += mylist[p][j]#y축
                except:
                    pass
            result -= mylist[i][j]
            result_plus.append(result)
            result = 0 #초기화

        
            #mylist[i-M:i+M][j-M:j+M]
            pointer = 1 # 초기화
            for p in range(M*2-1): #result_x 값 찾기  
                try:
                    
                    a = i-M+pointer
                    b = j-M+pointer
                    if 0<=a<N and 0<=b<N:
                        result += mylist[i-M+pointer][j-M+pointer]
                    pointer += 1
                except:
                    pass
            pointer = 1 # 초기화
            for p in range(M*2-1):
                    try:
                        a = i-M+pointer
                        b = j+M-pointer
                        if 0<=a<N and 0<=b<N:
                            result += mylist[i-M+pointer][j+M-pointer]
                        pointer += 1
                    except:
                        pass
            result -= mylist[i][j]
            result_x.append(result)
            result = 0
    #print(sorted(result_plus))
    #print(sorted(result_x))
    a = max(result_plus)
    b = max(result_x)
    print('#{} {}'.format(tc, max(a,b)))