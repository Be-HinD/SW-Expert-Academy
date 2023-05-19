T = int(input())

for tc in range(T):
    s = str(input())
    obj = list(s)
    obj = list(map(int, obj))
    cnt = 0
    length = len(obj)
    #dfs(s)
    start = [0] * len(s)
    i = 0
    while True:
        if ''.join(map(str, start)) == ''.join(map(str, obj)):
            print('#{} {}'.format(tc+1, cnt))
            break
        if start[i] != obj[i]:
            if obj[i] == 1:
                cnt += 1
                for w in range(i, length):
                    start[w] = 1
            else:
                cnt += 1
                for w in range(i, length):
                    start[w] = 0
        i += 1

"""
while / if
"""