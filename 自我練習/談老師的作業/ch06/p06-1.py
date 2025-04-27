# list2=[34,67,234,134,76,123,34,234,56,67]
# list1=[45,67,12,34,23,234,445,0]
# list3=[]
# tol=0
# # for i in range(len(list2)):
#     #  tol+=list2[i]

# for i in range(len(list2)):
#     list3.append(list2[i]+list1[1])
    

# print(f"list 總合 {tol}")

# print("最大值",max(list3))
# print("最小值",min(list3))

# print("使用 SUM List3及函式",sum(list3))

#########
# list1=[[0],[1,2,3],[4,5,6],[11,12,13,14],[21,22,23,24,25],[31,32]]
# j=[]
# for i in range(len(list1)):
#     print(f'{i:<2}行 ',end="")
#     for j in range(len(list1[i])):
#         print(f'{list1[i][j]:>5}',end=" ")
    
#     print()
# try:
#     print(list1[2][23])
# except:
#     print("找不到")

# 自寫
import random as rnd
i_row,i_colum=map(int,(input(" input row colum ").split()))

# AA=[[rnd.randint(1,100),rnd.randint(1,100),rnd.randint(1,100)] for i in range(3)]
# lst2=[[rnd.randint(1,100) for j in range(i_row)] for i in range(i_colum)]

print(lst2)

for row in lst2:
    print(row)
    for j in row:
        print(j)
    
print('end')

# for i in range(len(lst2)):          #列數
#     for j in range(len(lst2[0])):   #每列長度(元素數量)
#         print('lst2[%d][%d] = %2d'%(i,j,lst2[i][j])) #依序列印元素內容
#     print()

for i in lst2:
    for j in i:
        print(f'{j:3d}',end="")
    print()


#########講義第六頁下
# import random

# lst2 = []   #建立空串列

# #輸入列數、行數
# row = int(input('Enter the number of row: '))  #列
# column = int(input('Enter the number of column: ')) #行

# for i in range(0,row):  #依照輸入值產生列數  
#     lst2.append([])
#     for j in range(0,column):   #依照輸入值產生每列元素
#         lst2[i].append(random.randint(1,50))
# print(lst2,'\n')
