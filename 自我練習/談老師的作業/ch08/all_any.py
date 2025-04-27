# all() 和 any() 是 Python 中非常實用的「邏輯工具函式」，用來針對一組條件進行整體判斷：

# ✅ all() 與 any() 用法與意思

# 函式	 中文意思	    回傳條件
# all()	全部為真才為真	如果全部元素都為 True → 回傳 True
# any()	任一為真就為真	如果有任一元素為 True → 回傳 True
# 🧪 範例：

a = [True, True, True]
b = [True, False, True]

print(all(a))  # ✅ True（全部為 True）
print(all(b))  # ❌ False（有 False）

print(any(a))  # ✅ True（至少有 True）
print(any([False, False, False]))  # ❌ False（全是 False）

# ✅ 常見搭配用法：迴圈條件判斷
# 例1：是否「全部」為數字

nums = ['123', '456', '789']
print(all(n.isdigit() for n in nums))  # ✅ True
# 例2：是否「至少有一個」大寫字母

text = "helloWorld"
print(any(c.isupper() for c in text))  # ✅ True，因為有 'W'

# 🧠 技巧小提醒：
# all() 常用於「格式整體驗證」（ex: 密碼全部符合）
# any() 常用於「至少有一個條件成立」（ex: 至少一個大寫）