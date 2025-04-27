# 9.	輸入資料到字典中，直到輸入鍵值為end結束，再輸入一個鍵值，進行搜尋這個鍵值是否存在字典中。

# DDD=set()
# dict1=[]

# while True:
#     i=""
#     i=str(input("Type a world=>"))
#     if i=="end":
#         break
#     DDD.add(i)
    
# for i in DDD:
#     dict1.append(i)
    
# find_1=str(input("尋找的文字"))

# if find_1 in dict1 :
#     print(f'有找到{find_1}')
# else:
#     print(f'沒有找到{find_1}')

#再次用字典解題
dict_1={}

print("請輸入 key:value 的資料(當key為end時結束)")
while True:
    key=input("請輸入鍵 Key=>")
    if key=="end":
        break
    value=input("請輸入值 value=>")
    dict_1[key]=value
    
find_key=input("請輸入要查的鍵 key=>")

for i,j in enumerate(dict_1,1):
    print(f'{i} 鍵={j} 值={dict_1[j]}')

if find_key in dict_1:
    print(f'有找到{find_key} 值為{ dict_1[find_key]}')
else:
    print(f"沒有找到鍵值{find_key}的值")