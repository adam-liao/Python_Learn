
# i_row,i_colum=map(int,input("input row colum" ).split())

# lst2=[i_row],[i_colum]

# for i in range(i_row):
#     for j in range(i_colum):
#         lst2.append[i] =str(i)+str(j)
# print(lst2)

# 第一題 輸入兩個正整數，當作串列的 列數 與 行數 ，每個位置存放內容為那個位置本身的 "行數索引值" 減去 "列數索引值" 的結果。
# def compute(lst):
#     for i in lst:
#         for j in i:
#             print(f'{j:2d}',end='')
#         print()
# #============以下為主程式======================
# # row,column =map(int,input("輸入列數 行數：").split())
# row,column =8,8

# lst=[]
# for i in range(row):
#     lst.append([])
#     for j in range(column):
#         lst[i].append(j-i)
# compute(lst)

#第二題 	輸入三位學生各五筆平時測驗成績，接著計算並輸出每位總分與平均
# import random as rnd

# scores=[[rnd.randint(60,100) for j in range(3)]for i in range(3)]
# # lst2=[[rnd.randint(60,100) for j in range(i_row)] for i in range(i_colum)]
# print(scores)
# for i in scores:
#     l=0
#     k=0
#     for j in i:
#         print(f'{j}')
#         k=k+j
#         l+=1
#     print(f' {k/l:6.2f}')   




