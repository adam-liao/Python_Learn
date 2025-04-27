# 3.	使用者輸入一個句子，(至少五個詞，以空白隔開，並輸出倒數三個詞)

i=map(str,input("key in a string=>").split())
j=tuple(i)
# j=list(i)
l=len(j)
# print(l)
k=3
for i_1 in range(l-3,l):
     print(j[i_1])



# # 2025/04/24-18:40
# sentence = input("Key in a sentence (至少五個詞, 用空白隔開): ")
# words = sentence.split()  # 直接得到 list
# count = len(words)

# if count < 5:
#     print("請輸入至少五個詞！")
# else:
#     print("\n倒數三個詞是：")
#     for word in words[-3:]:  # 用 slice 拿倒數三個
#         print(word)

