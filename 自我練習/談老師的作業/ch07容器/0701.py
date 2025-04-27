#1.	輸入數個整數並儲存至串列中，直到輸入-9999結束，再將此串列轉換成元組 ，最後顯示該元組 以及長度、最大值、最小值、總和。

# l1=[]

# while True:
#     try:
#         i=int(input("Key in "))
#         if i==9999:
#             break
#         if 0<= i <=100:
#             l1.append(i)
#         else:
#             print("input 0~100")
#     except:
#         print('illegal int')

# tuple1=tuple(l1)

# print(f'len {len(tuple1)} , max {max(tuple1)}, min { min(tuple1)}, sum {sum(tuple1)} ')

# # 2025/04/21-20:00
l1 = []

while True:
    try:
        i = int(input("請輸入整數（輸入 -9999 結束）："))
        if i == -9999:
            break
        if 0 <= i <= 100:
            l1.append(i)
        else:
            print("⚠️ 請輸入介於 0 到 100 的整數")
    except:
        print("❌ 輸入格式錯誤，請輸入整數")

# # 將串列轉換為元組
tuple1 = tuple(l1)

# # 顯示結果
print("元組內容：", tuple1)
print(f"長度：{len(tuple1)}")
print(f"最大值：{max(tuple1) if tuple1 else '無資料'}")
print(f"最小值：{min(tuple1) if tuple1 else '無資料'}")
print(f"總和：{sum(tuple1)}")


#-----------
