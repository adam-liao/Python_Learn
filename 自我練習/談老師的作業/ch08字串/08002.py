# 2.	使用者輸入一個字串，顯示每個字元對應的ASCII碼，並將ASCII碼加總
i=input("key in=>")
k=0
for j in i:
    k+=ord(j)
    print(f'{ord(j)}')
    
print("total:",k)

# 2025/04/24-18:35
# text = input("Key in => ")
# total = 0

# print("每個字元的 ASCII 值：")
# for char in text:
#     ascii_value = ord(char)
#     print(f'{char} : {ascii_value}')
#     total += ascii_value

# print(f"\n總和 Total: {total}")
