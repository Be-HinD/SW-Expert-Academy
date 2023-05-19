import sys
sys.stdin = open('input.txt', 'r')

Encoder = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/' ]
T = int(input())

for tc in range(1, T+1):
    word = list(input())
    value = ''
    for w in word:
        num = Encoder.index(w)
        # 2진수 변환 및 앞 0b 떼주기
        bin_num = str(bin(num))[2:]
        # 앞쪽 빈 부분을 0으로 채우기
        while len(bin_num) < 6:
            bin_num = '0' + bin_num
        value += bin_num
    result = ''

    # 10진수로 변환하기 위해 8자리로 만들어줌 (입력값*6) // 8
    for k in range(len(word)*6 // 8):
        # 10진수로 변환
        number = int(value[k*8 : k*8+8], 2)
        result += chr(number)
    print('#%d %s' % (tc, result))

"""
Base-64 이해 필요
"""