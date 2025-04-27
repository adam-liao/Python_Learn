# 題目：建立二個list ，第一個list 1放4種蔬菜名稱，第二個list 2放5種水果名稱。
# 將第二個list插入第一個list偶數的位置，如果空隔用完，這加在list 1的後面

# 步驟解析：
# 	1.	建立 list1（4種蔬菜）和 list2（5種水果）。
# 	2.	找出 list1 中的偶數位置（即索引為 0, 2, 4…）。
# 	3.	把 list2 的水果依序插入這些偶數位置。
# 	4.	如果 list2 還有剩下，則加在 list1 的最後面。

# 建立初始的 list
list1=['高麗菜','菠菜','空心菜','胡蘿蔔']
list2=['蘋果','香蕉','芒果','葡萄','西瓜']

#建立水果指標
fruit_index=0

# 插入水果到List偶數的位置
i=0

while i< len(list1) and fruit_index < len(list2):
    list1.insert(i,list2[fruit_index]) #將水果插入蔬菜中
    fruit_index+=1
    i+=2 #每次增加2，指到下一個要插入的位置(list1每插入一個水果會增加長度)

#如果水果還有剩下的，把他們加在最後面
if fruit_index < len(list2):
    list1.extend(list2[fruit_index:])
   
#顯示結果 
print(list1)
    

