#字串轉換練習
str1menu='''
1.capitalize()字串第1字元轉為大寫
2.lower()全小寫
3.upper()全大寫
4.title()第1個英文字第一個字元轉大寫
5.swapcase()將字串中字元反轉
6.replace(old,new)將old字串以new字串取代
'''
str1='''Strings in python are surrounded by either single quotation marks, or double quotation marks.
'''

print(str1menu)
# print(str1)
print("請輸入要轉換的方式")
while True:
    i=input("select 方式1-6 , m=menu,end=結束")
    if i== "end":
        break
    if i=='m':
        print(str1menu)
    elif i=="1":
        print(f"{str1.capitalize()}")
    elif i=="2":
        print(f"{str1.lower()}")
    elif i=="3":
        print(f"{str1.upper()}")
    elif i=="4":
        print(f"{str1.title()}")
    elif i=="5":
        print(f"{str1.swapcase()}")
    elif i=="6":
        print(f"{str1.replace(' ','**')}")
    else:
        print("請輸入選擇!")


# # 2025/04/24-19:10
# str1menu = '''
# 1. capitalize() 字串第 1 字元轉為大寫
# 2. lower()      全部轉小寫
# 3. upper()      全部轉大寫
# 4. title()      每個詞的第一字母大寫
# 5. swapcase()   大小寫互換
# 6. replace(old, new) 將空白字元替換為 **
# '''

# str1 = '''Strings in python are surrounded by either single quotation marks, or double quotation marks.'''

# print(str1menu)
# print("請輸入要轉換的方式")

# while True:
#     i = input("Select 方式 1-6 , m=menu, end=結束: ")
#     if i == "end":
#         break
#     elif i == "m":
#         print(str1menu)
#     elif i == "1":
#         print(str1.capitalize())
#     elif i == "2":
#         print(str1.lower())
#     elif i == "3":
#         print(str1.upper())
#     elif i == "4":
#         print(str1.title())
#     elif i == "5":
#         print(str1.swapcase())
#     elif i == "6":
#         print(str1.replace(' ', '**'))  # ✅ 已修正引號
#     else:
#         print("⚠️ 請輸入正確的選擇！")


