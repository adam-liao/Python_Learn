

# 📝 字串重點整理

# 題號	重點練習	                     觀念與技巧說明
# 1	    enumerate() 顯示字元索引	     讓你學會列出字元與其順序
# 2	    ord() 計算 ASCII 和總和	         轉換字元成數字，用來做加總或加密
# 3	    split() + [-3:] 取倒數三詞	     學會如何用 list 處理字串分段
# 4	    upper() / title() 等字串格式轉換  各種大小寫轉換技巧
# 5	    count() 字元出現次數	          用來統計字元或子字串
# 6	    split() + sum() + map()	        處理多個數字並計算平均
# 7	    格式驗證：長度 + 數字 + 斷點符號	使用 split() 搭配 .isdigit()
# 8	    密碼格式驗證（長度、字元種類、大寫）  串聯邏輯條件與 any() 搭配 isupper()


# 🧰 二、Python 常用字串方法整理

# 方法	                 功能說明
# str.upper()	        所有字元轉大寫
# str.lower()	        所有字元轉小寫
# str.title()	        每個單字開頭大寫
# str.capitalize()	    只有第一個字元大寫，其餘小寫
# str.swapcase()	    大寫變小寫，小寫變大寫
# str.strip()	        去除前後空白
# str.replace(old, new)	替換指定字串
# str.split(sep)	    分割字串成 list
# 'sep'.join(list)	    把 list 合併成一個字串
# str.find(sub)	        傳回子字串第一次出現的位置，找不到傳回 -1
# str.count(sub)	    子字串出現次數
# str.startswith(sub)	是否以某子字串開頭
# str.endswith(sub)	    是否以某子字串結尾

# 🔐 三、常用字串驗證工具表（適合密碼 / 格式檢查）

# 驗證功能	             方法或語法
# 是否為純字母	          str.isalpha()
# 是否為純數字	          str.isdigit()
# 是否為字母+數字	       str.isalnum()
# 是否為全小寫	          str.islower()
# 是否為全大寫	          str.isupper()
# 是否包含大寫字母	       any(c.isupper() for c in str)
# 是否包含小寫字母	       any(c.islower() for c in str)
# 是否包含數字	           any(c.isdigit() for c in str)
# 是否符合長度要求	        len(str) >= 最小長度
# 是否符合格式（例如 email）	搭配 re.match() 或 split 判斷