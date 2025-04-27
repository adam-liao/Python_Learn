# 在一開始學的時候，常把List列表跟Tuple元組，弄混所以做了一個整理
# # 很多人學 Python 一開始也會把 tuple 和 list 混淆，現在正是釐清觀念的好時機，來一口氣搞懂兩者的差異 ✅

# 🆚 List vs Tuple 對照表

# 特性	         list 列表（✅可改）	       tuple 元組（🔒不可改）
# 語法	         [] 方括號	               () 小括號
# 是否可修改	   ✅ 可增刪改元素	        🔒 建立後不可改動
# 是否可加入元素	.append()、.extend()	❌ 不行
# 是否可刪除元素	.pop()、.remove()   	❌ 不行
# 使用時機	       資料會改變	            資料固定，不變才用
# 記憶體使用效率	比較高（稍慢）	          比較低（稍快）
# 可否巢狀使用	    ✅ 可以	                ✅ 也可以

# a = [1, 2, 3]
a=tuple()
a.append(4)       # OK
a[0] = 10         # OK
print(a)          # [10, 2, 3, 4]

# 🔒 Tuple：

b = (1, 2, 3)
b[0] = 10         # ❌ TypeError: 'tuple' object does not support item assignment

# ⚠️ 特別注意：
# 如果你少寫一層中括號，就會不小心變成 tuple：

x = [1, 2], [3, 4]  # ❌ 這是 tuple of list
print(type(x))     # <class 'tuple'>

# 要改成 list of list：

x = [[1, 2], [3, 4]]  # ✅ 二維 list

# 找錯誤 
# 💪這行程式碼：

furit = list('Hello')
furit.append(1,2,3,4,5) #這行是錯的
# 錯的地方在 .append() 的用法。

# 🔍 錯誤說明：
# 1️⃣ .append() 一次只能加入 一個元素

furit.append(1, 2, 3, 4, 5)  #這是錯的

# # ❌ TypeError: list.append() takes exactly one argument (5 given)
# ✅ 正確寫法有幾種：
# ✅ 方法一：如果你要加入整個 [1, 2, 3, 4, 5] 當成一個項目：

furit.append([1, 2, 3, 4, 5])
# 結果是：

['H', 'e', 'l', 'l', 'o', [1, 2, 3, 4, 5]]

# ✅ 方法二：如果你要把這幾個數字逐一加入清單
# 用 .extend() 或 for 迴圈：


# 用.extend()：

furit.extend([1, 2, 3, 4, 5])

# 結果是：

['H', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5]

#for 迴圈：

for i in [1, 2, 3, 4, 5]:
    furit.append(i)




# ✅ 你的程式碼其實是沒錯的：

fruit = list('Hello')
fruit.extend([1, 2, 3, 4, 5]) #用list 包起來再轉成元組

for i in fruit:
    print(i, end='')
    
# 這段程式輸出的應該是：

#Hello12345

###### 以下還有常見的錯誤

# 你這樣寫幾乎快對了，但目前還有一個小錯誤 👀
# 來看一下你的程式碼：


fruit = [1,5,3],[7,8,4,2],[23,45,23,12,567,78]
fruit.pop()

# ❌ 錯誤點
# 這一行：
fruit = [1,5,3],[7,8,4,2],[23,45,23,12,567,78]
# 其實不是把三列放進一個 二維 list，而是：
# 🔍 建立了一個「元組」（tuple）
# 等於：

fruit = ([1,5,3], [7,8,4,2], [23,45,23,12,567,78])  # ⬅️ tuple，有三個 list

# 所以 fruit.pop() 的錯誤訊息會是：
# AttributeError: 'tuple' object has no attribute 'pop'
# ✅ 正確做法：請用中括號 [] 包起來形成二維 list

fruit = [
    [1,5,3],
    [7,8,4,2],
    [23,45,23,12,567,78]
]

fruit.pop()

# 這樣才會刪除最後一列（即 [23,45,23,12,567,78]）

# 可以印出來驗證看看：

print(fruit)
# 輸出：[[1, 5, 3], [7, 8, 4, 2]]

# 🧠 小總結

# 錯誤寫法	結果	問題
# a = [1,2],[3,4]	是 tuple	無法使用 .pop()
# ✅ a = [[1,2],[3,4]]	是 list	可使用 .pop() 刪除最後一列