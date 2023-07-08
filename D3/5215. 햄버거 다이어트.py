import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def dfs(index,sum_flavor=0,sum_kal=0):
    global max_flavor
    if sum_kal > l:
        return
    if max_flavor < sum_flavor:
        max_flavor = sum_flavor
    if index == n:
        return
    flavor,kal=kal_list[index]
    dfs(index+1,sum_flavor + flavor, sum_kal + kal)
    dfs(index+1,sum_flavor,sum_kal)

for tc in range(1,T+1):
    n,l = map(int,input().split())
    kal_list = [list(map(int,input().split())) for i in range(n)]
    max_flavor = 0
    dfs(0)
    print('#%d %d' % (tc,max_flavor))