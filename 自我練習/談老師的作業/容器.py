# list1=[]

# list1=list( n  for n in range(1,100) if n %14 )

# print(*(list1))



list2="today is a goodday"
# list5=list(list2)
# print(list3)

# print(*(list2[n]+"\n" for n in range(len(list2))))

# print(list2[5:len(list2)])

# apple=[7.6,3,4,6,7,8,2,3,55]
# print(sum(apple),min(apple),max(apple))

# 
# print(*list5[3:12])
# print(list2.find('o'))
# print(list2.rfind('d'))
# print(list3)
# list3.insert(n, for n in range(len(list4))list4[i])
# print(list3)
# for i in range(3):
#     list1.append(input("請輸入字元 "))
# else:
#     print(list1)
# list3=[]
# for i in range(3):
#     list3.append(input("請輸入字元 ") )
# list3=[int(input("input ")) for i in range(3)]
# print(list3)

#輸入序列的幾種寫法
# list1=[]
# list1=[int(input(" input ")) for i in range(3)]
# print(list1)
# list1.append(input("append ") for i in range(2))
# print(*list1)
# list3.remove(input(' remove'))

# print(list3)
# list3.append(list4)
list3=["apple","orange","banana"]
list4=["pi apple","green orange","lemmo"]
# list3.extend(list4)
# list3.append('yellow Banana')
# list3.append('apple')
# list3+=list4
# print(list3)
# c=list3.count('apple')
# print(c)

# try:
#     print(f' {list3.index('pip apple')}')
# except:
#     print("沒有找到")


#在list3 的偶數 插入 list4, 如果最後list4還有剩就全部右在list3的後面
# fruit_index=0
# i=1

# while i < len(list2) and fruit_index < len(list4):
#     list3.insert(i,list4[fruit_index])
#     fruit_index+=1
#     # print(f'loop{i:2d} {list3}')
#     i+=2

# if fruit_index< len(list4):
#     list3.extend(list4[fruit_index:])
# print(list3)
# list3.sort(reverse=True)
# print("reSort ",list3)

# 亂七八糟
# list3.reverse()
# print("reverse  ",list3)

# print(" find apple in list3") if "pi apple" in list3 else print(" not find")

# # for i in list3:
# #     print(i)

# for i in range(len(list3)):
#     if list3[i]=='apple':
#         list3.pop(i)

# print(list3)

#第一題 樂透抽獎
import random as rnd

# total_number=49
# org_number= [i for i in range(1,total_number+1)]
# print("待抽的號碼\n",org_number)

# get_number=[]
# for i in range(1,7):
#     lock_number=rnd.randint(0,total_number-1)
#     get_number.append(org_number[lock_number])
#     org_number.remove(lock_number)
#     # print(lock_number,end=' ')
#     total_number-=1
# else:
#     print("")
# get_number.sort()
# print('幸運數字',*(get_number))
# print("未被抽中的號碼\n",*(org_number))

#第二題 這一題還有些觀念要黎清
# import random as rnd
# total_number=49
# org_number= [i for i in range(1,total_number)]
# print("待抽的號碼\n",org_number)
# picked=rnd.sample(org_number,6)
# for number in picked:
#     org_number.remove(number)
# print(*picked)

#第三題
# type_number=[]
# for i in range(1,13):
#     type_number.append(int(input(f"{i} 輸入一整數")))
# else:
#     type_number.sort()
# print(type_number)

# 第四題
# poke_number=[]
# poke_number=[n for n in range(1,13)]
# print(*(poke_number))
# get_number=[]
# get_number.append(rnd.sample(poke_number,5))
# ss=sum(*get_number)
# print(ss,"----",*get_number)

# 第五題
# type_number=[]
# for i in range(1,11):
#     type_number.append(int(input(f"{i} 輸入一整數")))
# else:
#     type_number.sort(reverse=True)
# print(type_number[0:3])

#第六題
# for i in range(1,11):
#     type_number.append(int(input(f"{i} 輸入一整數")))
# type_number=[1,2,14,5,6,6,7,8,9,4]
# max_count=[]
# k=0
# for i in range(len(type_number)):
#     k=0
#     for j in range(len(type_number)):
#         if type_number[i]>type_number[j]:
#             k+=1
#     max_count.append(k)
# print(type_number,"\n在序列中最大值為",type_number[max_count.index(max(max_count))])


#第七題
# type_number=[]
# x=0
# k=0
# while True:
#     x=int(input('input a number ,999=Quit'))
#     if x == 999:
#         break
#     type_number.append(x)
#     k=k+1

# max_number=max(type_number)
# min_number=min(type_number)
# sum_number=sum(type_number)
# print(f'最大值 {max_number}  最小值 {min_number} 加總 {sum_number} avg {sum_number/k:8.2f}')

#第八題
# names={'bob':0,'anna':0,'adam':0,'julia':0,'lydia':0}
names={'bob':60,'anna':90,'adam':70,'julia':80,'lydia':77}

# for name in names: #取出List有鍵值的資料
#     while True:
#         try:
#             score=int(input(f' 輸入{name}的成績 '))
#             if 0<= score <= 100:
#                 names[name]=score
#                 break
#             else:
#                 print("請輸入成績0～100")
#         except:
#             print("請輸入整數")
#     else:
#         #輸入錯誤時會到這裡，然後再重新輸入
#         print("輸入下一位")

# print(names)

def get_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "E"

	# •	item 是你 sorted() 處理的 每一個元素
	# •	item[1] 是你要用來「排序依據的值」
	# •	lambda 是匿名函式（像快速定義一個小函式）
    #sorted(employees.items(), key=lambda item: item[1])
    #排序字典 items() ➜ 依「值」排序（成績）

for name,score in sorted(names.items(),key=lambda item:item[1],reverse=True):
    print(f'{name.capitalize():<6} 成績：{score:>3}分 等級：{get_grade(score)}' )
        