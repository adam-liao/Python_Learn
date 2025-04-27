# 題目：建立二個list ，第一個list 1放4種蔬菜名稱，第二個list 2放5種水果名稱。
# 將第二個list插入第一個list偶數的位置，如果空隔用完，這加在list 1的後面

# 步驟解析：
# 	1.	建立 list1（4種蔬菜）和 list2（5種水果）。
# 	2.	找出 list1 中的偶數位置（即索引為 0, 2, 4…）。
# 	3.	把 list2 的水果依序插入這些偶數位置。
# 	4.	如果 list2 還有剩下，則加在 list1 的最後面。

list1=['高麗菜','菠菜','空心菜','胡蘿蔔']
list2=['蘋果','香蕉','芒果','葡萄','西瓜']

fruit_index=0
i=0

while i< len(list1) and fruit_index < len(list2):
    list1.insert(i,list2[fruit_index])
    fruit_index+=1
    i+=2
    
if fruit_index < len(list2):
    list1.extend(list2[fruit_index:])
    
print(list1)
    

