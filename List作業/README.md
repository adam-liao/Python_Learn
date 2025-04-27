# List 作業的註解

### 蔬菜水果插隊排序.py
註解在程式中
```Python

list1=['高麗菜','菠菜','空心菜','胡蘿蔔']
list2=['蘋果','香蕉','芒果','葡萄','西瓜']

fruit_index=0
i=0

while i< len(list1) and fruit_index < len(list2):
    list1.insert(i,list2[fruit_index])
    fruit_index+=1
    i+=2
    
if fruit_index < len(list2):
    list1.extend(list2[fruit_index:])
    
print(list1)
 
```
**結果為**
['蘋果', '高麗菜', '香蕉', '菠菜', '芒果', '空心菜', '胡蘿蔔', '葡萄', '西瓜']