#3.	輸入至少五個字串至元組 ，直到輸入’end’結束，接著輸出這個元組 ，再分別顯示元組 的第一個元素到第三個元素，和倒數第三個元素。

T1=[]

while True:
    i=""
    i=str(input(" Key In "))
    if i=="end":
        break
    T1.append(i)

T1=tuple(T1)
print(T1)
print(T1[0:2])
print(T1[-3])

# # 2025/04/21-20:15
# T1 = []

# while True:
#     i = input("請輸入字串（輸入 end 結束）：")
#     if i == "end":
#         break
#     T1.append(i)

# if len(T1) < 5:
#     print("⚠️ 請至少輸入五個字串！目前只輸入了", len(T1), "個")
# else:
#     T1 = tuple(T1)
#     print("輸入的元組：", T1)
#     print("前三個元素：", T1[0:3])
#     print("倒數第三個元素：", T1[-3])
