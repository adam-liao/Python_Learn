
# 3.	建立一個3 * 3的串列矩陣，內容為鍵盤輸入的整數(不能重複)，接著輸出矩陣最大與最小值的索引。

score=[]

for j in range(3):
    row=[]
    for i in range(3):
        row.append(int(input("輸入成績 ")))
    score.append(row)
    
    print(score)
print()

max_val=-999
min_val=999
max_pop=(0,0)
min_pop=(0,0)

# 正確作法：手動用巢狀迴圈掃描「值」的 (列, 行) 索引
for i in range(3):
    for j in range(3):
        val=score[i][j]
        if val>max_val:
            max_val=val
            max_pop=(i,j)
        if val<min_val:
            min_val=val
            min_pop=(i,j)
       
print(f'最大值 {max_val} , 最小值 {min_val}，索引值{max_pop},{min_pop}')
