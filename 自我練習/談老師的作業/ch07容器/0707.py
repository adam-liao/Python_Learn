# 7.	自行輸入兩個字典，以輸入值end作為結束，將這兩個字典合併，根據key值字母，由小到大排序輸出，如有重複key值，後輸入的key值覆蓋前面的key值。

dict1={}
dict2={}


def keyin(dictA):
    print("請輸入鏈跟值，當鍵為end時結束輸入")
    while True:
        k=input('請輸入一個鍵=>')
        if k=='end':
            break
        v=input("請輸入一個值=>")
        dictA[k]=v

print("請輸入第一個字典")       
keyin(dict1)
print("請輸入第二個字典")       
keyin(dict2)
        
dict1.update(dict2)
print("\n列出合併字典")
for i,j in enumerate(dict1,1):
    print(f'{i} {j}:{dict1[j]}')
print("\n排序結果")
for k,v in sorted(dict1.items()):
    print(f'{k: >8}:{v}')
    
    
    
# # 7.	自行輸入兩個字典，以輸入值end作為結束，將這兩個字典合併，根據key值字母，由小到大排序輸出，如有重複key值，後輸入的key值覆蓋前面的key值。

# dict1={}
# dict2={}


# def keyin(dictA):
#     print("請輸入鏈跟值，當鍵為end時結束輸入")
#     while True:
#         k=input('請輸入一個鍵=>')
#         if k=='end':
#             break
#         v=input("請輸入一個值=>")
#         dictA[k]=v

# print("請輸入第一個字典")       
# keyin(dict1)
# print("請輸入第二個字典")       
# keyin(dict2)
        
# dict1.update(dict2)
# print("\n列出合併字典")
# for i,j in enumerate(dict1,1):
#     print(f'{i} {j}:{dict1[j]}')
# print("\n排序結果")
# for k,v in sorted(dict1.items()):
#     print(f'{k: >8}:{v}')