# 4.  讓使用者建立2個 2* 2的串列矩陣內容，內容為鍵盤輸入的整數，接著輸出這兩個矩陣內容及相加結果。

score=[]
score_a=[]

for i in range(2):
    row=[]
    for j in range(2):
        row.append(int(input("B key in")))
    score.append(row)

for i in range(2):
    row=[]
    for j in range(2):
        row.append(int(input("A key in ")))
    score_a.append(row)

print(score)
print(score_a)

for i in range(2):
    for j in range(2):
        print(score[i][j]+score_a[i][j],end=" ")
    print()