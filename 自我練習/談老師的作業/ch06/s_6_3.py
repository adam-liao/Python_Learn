#第三題 建立一個3 * 3的串列矩陣，內容為鍵盤輸入的整數(不能重複)，接著輸出矩陣最大與最小值的索引。
# scores=[[]*3]*3
scores=[]
lst1=[]
def key_in_list(lst,i_row,i_col):
    for i in range(i_row):
        lst_append([])
        for j in range(i_col):
            lst.append(int(input(f' input {i}*{j} =')))
            print(scores[i])
    # lst=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print("list=",scores)
i_max=0
s_max=""

i_min=0
s_min=""
#問題當由1-9時,最小值無法顯示
for i in range(len(scores)):
    for j in range(len(scores[i])):
        print(scores[i][j])
        if i_max <  scores[i][j]:
            i_max=scores[i][j]
            s_max=str(i)+'X'+str(j)
        if i_min >  scores[i][j]:
            i_min=scores[i][j]
            s_min=str(i)+'X'+str(j)

print(f' max{i_max} in {s_max} , min{i_min} in {s_min}')


### 老師的寫法 看不懂
def max_min():
    a = c = mat [0][0]      #設定變數 a、c等於串列mat[0][0]的內容(比大小初始值)
    b = d = 0               #設定c、d為0 (索引值用)
    
    for i in range (0,m):   #使用迴圈，逐一檢查"每一列"中的最大值
        if a < max(mat[i]): #使用max函數查詢 mat第[i]列的最大值和a的內容比較
            a = max(mat[i]) #若a < mat[i]列中，最大值，就改寫a的內容
            b = i           #把b 設為目前最大值 所在列的編號
     
        if c > min(mat[i]):
            c = min(mat[i])
            d = i

    e = mat[b].index(a)
    print(f"mat[{b}][{mat[b].index(a)}] 最大值：{a}")  #用index索引mat[b]列中，a的位置  
    print(f"mat[{d}][{mat[d].index(c)}] 最小值：{c}") 

#====================以下為主程式==============================

mat = []
m = 3

for i in range(0,m):
    mat.append([])
    for j in range(0,m):
        mat[i].append(eval(input(f"輸入整數[{i}][{j}]:")))

max_min()