for tc in range(1, 11):
    num = int(input())
    height = list(map(int, input().split()))
    result = 0
    cnt = 0
    left = 0
    right = 0
    for i in range(len(height)):
        try:
            left = max(height[i-2], height[i-1])
            right = max(height[i+1], height[i+2])
            sum = max(left, right)
            if height[i] > sum:
                result += height[i] - sum
            else:
                left = 0
                right = 0
                sum = 0
        except:
            left = 0
            right = 0
            sum = 0
    print('#{} {}'.format(tc, result))

"""
단순 조건문
"""