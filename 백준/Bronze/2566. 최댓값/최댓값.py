matrix=[]
for n in range(9):
    p=list(map(int,input().split()))
    matrix.append(p)
max_num=0
max_row=0
max_col=0
for row in range(9):
    for col in range(9):
        if max_num <= matrix[row][col]:
            max_num = matrix[row][col]
            max_row=row+1
            max_col=col+1
print(max_num)
print(max_row, max_col)