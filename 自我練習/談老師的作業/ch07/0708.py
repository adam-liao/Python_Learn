# 8.	輸入顏色字典color_dict 內容，直到鍵值輸入end為止。再依據鍵值字母由小到大排序輸出
color_dict={}

while True:
    i=input('請輸入顏色名稱=>')
    if i=="end":
        break
    j=input('請輸入顏色的值=>')
    color_dict[i]=j
    
for i,j in sorted(color_dict.items()):
    print(f'{i:>8}: {j}')

# # 2025/04/21-20:50
# color_dict = {}

# # 輸入 key:value，直到 key 是 end 為止
# while True:
#     key = input("請輸入顏色名稱（key，輸入 end 結束）：")
#     if key == "end":
#         break
#     value = input("請輸入顏色的值（value）：")
#     color_dict[key] = value

# # 顯示原始字典（可選）
# print("\n輸入的顏色字典：")
# print(color_dict)

# # 依照 key 排序後輸出
# print("\n排序後的結果（依鍵名稱排序）：")
# for k, v in sorted(color_dict.items()):  # 預設就是依 key 排序
#     print(f"{k:>8} : {v}")