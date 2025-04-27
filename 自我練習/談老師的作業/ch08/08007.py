# 7.	使用者輸入一串序號，格式為ddd-dd-ddd ，d為數字。檢查輸入格式正確，則輸出"格式正確！"，否則輸出"格式錯誤！"

i=map(str,input("key in ddd-dd-dd , d is a number").split('-'))
j=list(i)
print(j)
for k,l in enumerate(j,1):
    print(f'{k} {l} ={l.isdigit()}')


# # 2025/04/24-19:00
# serial = input("Key in serial number (格式 ddd-dd-ddd)：")
# parts = serial.split('-')

# if len(parts) == 3 and all(part.isdigit() for part in parts):
#     if len(parts[0]) == 3 and len(parts[1]) == 2 and len(parts[2]) == 3:
#         print("格式正確！")
#     else:
#         print("格式錯誤！（長度不符）")
# else:
#     print("格式錯誤！（分段數量或非數字）")
