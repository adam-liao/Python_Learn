# 班上有三個同學 annie,lydia,mary, 學科有 國文、數學、英文，請輸入三個人的三個學科的成績，最後算出第一名至第三名，並印出來

# 可以！這題我們要做的是：
# 輸入三個學生、三個科目的成績
# 計算每個學生的總分
# 根據總分排序，列出第一名至第三名
# 這裡有一個完整的程式範例（附上註解說明）：

# 2025/04/16-20:10
students = ["annie", "lydia", "mary"]
subjects = ["國文", "數學", "英文"]

# 儲存成績用的字典，每個學生對應一個成績小字典
scores = {}

# 輸入每個學生每個科目的成績
for student in students:
    print(f"\n請輸入 {student.capitalize()} 的成績：")
    scores[student] = {}
    for subject in subjects:
        while True:
            try:
                score = int(input(f"{subject}："))
                if 0 <= score <= 100:
                    scores[student][subject] = score
                    break
                else:
                    print("請輸入 0~100 之間的整數")
            except:
                print("⚠️ 請輸入正確的整數")

# 計算總分並建立新列表
total_scores = []
for student in students:
    total = sum(scores[student].values())
    total_scores.append((student, total))

# 排名（由高至低）
ranked = sorted(total_scores, key=lambda x: x[1], reverse=True)

# 印出排名結果
print("\n📊 成績排名：")
for i, (name, total) in enumerate(ranked, start=1):
    print(f"{i}. {name.capitalize()}：總分 {total} 分")
# 範例輸出：
# 請輸入 Annie 的成績：
# 國文：90
# 數學：95
# 英文：88

# 請輸入 Lydia 的成績：
# 國文：85
# 數學：91
# 英文：90

# 請輸入 Mary 的成績：
# 國文：80
# 數學：82
# 英文：84

# 📊 成績排名：
# 1. Annie：總分 273 分
# 2. Lydia：總分 266 分
# 3. Mary：總分 246 分



########第二種寫法
# 非常適合用字典來表示學生資料！這樣資料的結構會更清晰，而且操作更方便。

# 我們來比較一下兩種做法：

# ✅ 使用「字典格式」儲存學生資料（推薦）

# 2025/04/16-20:20
students = {
    "annie": {"國文": 90, "數學": 95, "英文": 88},
    "lydia": {"國文": 85, "數學": 91, "英文": 90},
    "mary": {"國文": 80, "數學": 82, "英文": 84}
}
# 這樣的好處是：
# 結構化：可以一眼看出每個學生的成績
# 好查詢：例如 students["lydia"]["英文"] 就是 Lydia 的英文分數
# 好加總：sum(students["annie"].values()) 就是 Annie 的總分

# 🚫 使用平行列表（不推薦）
names = ["annie", "lydia", "mary"]
chinese = [90, 85, 80]
math = [95, 91, 82]
english = [88, 90, 84]

# 雖然也能算，但資料分離、容易出錯，例如 math[1] 是誰的數學？你得記住 lydia 是第 2 位，非常不好管理。

# ✅ 使用字典 + 輸入 + 排名的完整範例
# 如果你想用字典結構從頭輸入資料並完成排名，這是更完整的寫法：


# 2025/04/16-20:25
students = {}
subjects = ["國文", "數學", "英文"]
names = ["annie", "lydia", "mary"]

# 資料輸入
for name in names:
    print(f"\n請輸入 {name.capitalize()} 的成績：")
    students[name] = {}
    for subject in subjects:
        while True:
            try:
                score = int(input(f"{subject}："))
                if 0 <= score <= 100:
                    students[name][subject] = score
                    break
                else:
                    print("請輸入 0~100 之間的整數")
            except:
                print("⚠️ 請輸入正確的整數")

# 計算總分並排序
ranking = []
for name, score_dict in students.items():
    total = sum(score_dict.values())
    ranking.append((name, total))

ranking.sort(key=lambda x: x[1], reverse=True)

# 顯示排名
print("\n📊 成績排名：")
for i, (name, total) in enumerate(ranking, start=1):
    print(f"{i}. {name.capitalize()}：總分 {total} 分")
    
    
    
#####第三種寫法

# 這樣的寫法非常棒，而且已經把資料格式整理得很清楚了，接下來只要加上總分計算與排名排序的程式就好了 👍
# ✅ 接續你的 students 字典來做排名的範例：

# 2025/04/16-20:30
students = {
    "annie": {"國文": 90, "數學": 95, "英文": 88},
    "lydia": {"國文": 85, "數學": 91, "英文": 90},
    "mary": {"國文": 80, "數學": 82, "英文": 84}
}

# 建立 (名字, 總分) 的列表
ranking = []
for name, subjects in students.items():
    total = sum(subjects.values())
    ranking.append((name, total))

# 依總分由高至低排序
ranking.sort(key=lambda x: x[1], reverse=True)

# 顯示排名結果
print("📊 成績排名：")
for i, (name, total) in enumerate(ranking, start=1):
    print(f"{i}. {name.capitalize()}：總分 {total} 分")
    
# 💡 執行結果會是：

# 📊 成績排名：
# 1. Annie：總分 273 分
# 2. Lydia：總分 266 分
# 3. Mary：總分 246 分
# 如果你想要同時顯示每個人各科成績 + 平均分數，也可以加上這段：

for name, subjects in students.items():
    total = sum(subjects.values())
    avg = total / len(subjects)
    print(f"{name.capitalize()}：{subjects} ➜ 平均：{avg:.2f} 分")







# 程式解說，這段程式碼是用來計算每位學生的總分，並把結果存到 ranking 這個列表中。讓我一句一句地說明：
for name, subjects in students.items():
    total = sum(subjects.values())
    ranking.append((name, total))

# 拆解！
for name, subjects in students.items():

# ✅ 這行的意思是：
# students.items() 會把整個 students 字典的 key 和 value 一起拿出來。
# name 是學生的名字（像 "annie"）
# subjects 是該學生的成績字典（像 {"國文": 90, "數學": 95, "英文": 88}）

# 👉 簡單說，每次迴圈會拿出一位學生的 名字與他的所有成績

    total = sum(subjects.values())

# ✅ 這行的意思是：

# subjects.values() 會拿出成績字典的所有分數值（例如 [90, 95, 88]）

# sum(...) 會把這些分數加總，得到總分

# 👉 結果會像：total = 273

    ranking.append((name, total))

# ✅ 這行的意思是：
# 把 name 和 total 做成一個小 tuple (name, total)
# 然後加進去 ranking 這個列表中

# 👉 結果像：ranking = [("annie", 273), ("lydia", 266), ("mary", 246)]

# 🧠 總結這段做了什麼：
# 它把每個學生的：
# 名字（key）
# 總分（sum of 成績）
# 放到 ranking 裡面，之後就可以拿這個列表來做排序與排名！
# 如果你想印出中間過程，加入 print(name, total) 就可以看到每一步算出來的結果。




#######延伸超重要的
# 取得值 subjects.values() 那鍵也可以取出嗎？
# 除了用 subjects.values() 取得「值（分數）」，你也可以取得「鍵（科目名稱）」，用的就是：

subjects.keys()

# 📘 補充說明
# 假設：

subjects = {"國文": 90, "數學": 95, "英文": 88}

# 你可以這樣取得：

# 語法	             取得內容	                 範例結果
# subjects.keys()	所有「科目名稱」	          dict_keys(['國文', '數學', '英文'])
# subjects.values()	所有「成績」	              dict_values([90, 95, 88])
# subjects.items()	同時取得「科目名稱 和 分數」	[('國文', 90), ('數學', 95), ('英文', 88)]

# ✅ 實用範例：列出每個科目的分數

for subject, score in subjects.items():
    print(f"{subject}：{score} 分")
# 💡會印出：
# 國文：90 分
# 數學：95 分
# 英文：88 分

# 想要列出「每位同學的每一科成績」也可以這樣寫：

for name, subjects in students.items():
    print(f"\n{name.capitalize()} 的成績：")
    for subject, score in subjects.items():
        print(f"  {subject}：{score}")


# 國文為鍵，90為值，那annie稱為什麼？

students = { "annie": {"國文": 90, "數學": 95, "英文": 88},}

# 這個問題問得超清楚 👍 我們來一步一步看：

# 📦 結構分析

students = {
    "annie": {
        "國文": 90,
        "數學": 95,
        "英文": 88
    }
}

# 這是「巢狀字典」結構，可以理解成：
# students 是一個大字典
# "annie" 是這個字典中的一個鍵（key）
# {"國文": 90, "數學": 95, "英文": 88} 是對應的值（value），也是一個字典

# 🔍 所以問的重點是：
# 「國文」是鍵，90 是值，那 "annie" 是什麼？

# 👉 答案是：annie 是 students 字典中的「鍵」。

# 更完整的關係如下：

# 層級	     鍵	                值
# 外層字典   students	        "annie"	{"國文": 90, "數學": 95, "英文": 88}
# 內層字典   students["annie"]	"國文"	90
#                              "數學"	95
#                              "英文"	88


# ✅ 所以你可以這樣取得資料：

students["annie"]             # 取出 annie 的整個成績字典
students["annie"]["國文"]     # 取出 annie 的國文分數（90）

