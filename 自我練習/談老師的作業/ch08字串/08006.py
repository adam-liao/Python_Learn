# 6.	使用者輸入一個字串，字串為五個數字，以空白隔開，加總五個數字並計算平均

i=map(str,input("Keyin 5 number=>").split())
j=tuple(i)
print('+'.join(j))
print(eval('+'.join(j)))

# # 2025/04/24-18:55
# nums = input("Key in 5 numbers (用空白隔開) => ").split()

# if len(nums) != 5:
#     print("⚠️ 請輸入剛好五個數字！")
# else:
#     nums = list(map(int, nums))  # 轉成整數
#     total = sum(nums)
#     average = total / 5
#     print("加總表示式：", " + ".join(map(str, nums)))
#     print(f"總和：{total}")
#     print(f"平均：{average:.2f}")
