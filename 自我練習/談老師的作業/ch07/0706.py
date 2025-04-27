# 6.	課程分組，分為X與Y兩組，輸入X和Y兩組需要學習的科目到集合中，以字串”end”作為結束，請依序分行顯示
# (1)	X組和Y組所有的科目
# (2)	X組和 Y組共同科目
# (3)	Y組有但是X組沒有的科目
# (4)	X有Y沒有以及Y有X沒有的科目
# (5)	X組: 國文、英文、數學乙、地理、歷史。 Y組：國文、數學甲、英文、物理、化學
# 2.3	集合聯集、交集、差集、對稱差
# 集合在運用上，常見使用聯集(union)、交集(intersection)、差集(difference)、對稱差集(symmetric difference)四種

setx=set()
sety=set()
ans=set()
def keyint(seta,i):
    print(f"請輸入{i}組的學習課目，輸入end為結束")
    while True:
        k=input("請輸入科目=>")
        if k=='end':
            break
        seta.add(k)

print('請輸入X組')
keyint(setx,'X')

print('\n請輸入Y組')
keyint(sety,'Y')

ans=setx.union(sety)
print(f"聯集為{ans}\n")

ans=setx.intersection(sety)
print(f"交集為{ans}\n")

ans=setx.difference(sety)
print(f'差集為 {ans}\n')

ans=setx.symmetric_difference(sety)
print(f'對稱差為 {ans}')

