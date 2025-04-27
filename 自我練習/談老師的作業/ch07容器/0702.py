#2.	輸入數個整數並建立兩個元組 ，輸入-9999結束，將此兩元組 合併並從小到大排序，顯示排序前的元組 和排序後的串列。
def keyin(L1):
    while True:
        try:
            i=int(input("Key in "))
            if i == -9999:
                break
            if 0<= i <=100:
                L1.append(i)
            else:
                print(" input 0-100")
        except:
            print("illegal number")
        
D1=[]
D2=[]
DT=[]
keyin(D1)
print("D1=>",D1)
keyin(D2)
print("D2=>",D2)
D1.extend(D2)
D1.sort()
DT=tuple(D1)

print(f'{DT}')

# # 2025/04/21-20:10
# def keyin():
#     L = []
#     while True:
#         try:
#             i = int(input("請輸入整數（輸入 -9999 結束）："))
#             if i == -9999:
#                 break
#             if 0 <= i <= 100:
#                 L.append(i)
#             else:
#                 print("⚠️ 請輸入 0～100 的整數")
#         except:
#             print("❌ 非法輸入，請輸入整數")
#     return tuple(L)  # 直接回傳元組

# # 取得兩個元組
# D1 = keyin()
# print("D1 元組：", D1)

# D2 = keyin()
# print("D2 元組：", D2)

# # 合併並轉為串列排序
# merged_list = list(D1 + D2)
# merged_list.sort()

# # 顯示排序後結果
# print("排序後的串列：", merged_list)