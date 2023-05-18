def typetest(M):
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            row = M[i][j]
            col = M[j][i]
            if row_num[row] or col_num[col]:
                return 0
            else:
                row_num[row] = 1
                col_num[col] = 1
            # 3x3 행렬 검사
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = M[r][c]
                        if square[num]: return 0
                        square[num] = 1
    return 1


T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = typetest(sudoku)
    print('#{} {}'.format(tc, result))

"""
***재검증 필요***
"""