# 10.	輸入五筆資料放在 tuple10 的元組 ，之後印出元組 每一個元素，以及找出此元組 最大值、最小值、總和。

list1=[]

for i in range(5):
    j=int(input("Key in=>"))
    list1.append(j)

t=tuple(list1)
print(f'所有元素{t} 最大值{max(t)} 最小值{min(t)} 總合{sum(t)}')