'''
4.  讓使用者建立2個 2* 2的串列矩陣內容，內容為鍵盤輸入的整數，接著輸出這兩個矩陣內容及相加結果。
'''
#串列輸入函式：
def Input(mat,row,col):
    for i in range(ROWs):
        mat.append([])
        for j in range (COLs):
            print('[%d][%d]:'%((i ),(j )),end='')
            mat[i].append(eval(input('輸入數字')))

def compute(mat, row, col):
    a = 0
    for i in range(row):
        for j in range(col):
            print( f"{mat[i][j]}",end=" ")
        print()
#==========================================
ROWs = 2
COLs = 2
mat0 = [[0,0],[0,0]]
mat1 = []
mat2 = []

print('輸入第一組資料：')
Input(mat1,ROWs,COLs)
print('輸入第二組資料：')
Input(mat2,ROWs,COLs)

print("第一組矩陣：")
compute(mat1,ROWs,COLs)
print("第二組矩陣：")
compute(mat2,ROWs,COLs)

print('兩組矩陣和：')
for i in range (ROWs):
    for j in range(COLs):
        mat0[i][j] = mat1[i][j]+mat2[i][j]
        print(f"{mat0[i][j]}",end = ' ')
        # print('%d'%(mat1[i][j]+mat2[i][j]),end = ' ')
    print()
