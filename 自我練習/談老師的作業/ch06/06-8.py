# # 題	使用lotto ()產生6個樂透號碼，並以main()函式呼叫5次lotto()函式產生五組號碼，並由小到大排序出來。

# import random as rnd

# lotto_bor=[ i for i in range(1,50)]
# get_bor=[]

# print(lotto_bor)

# def lotto():
#     i=rnd.randint(lotto_bor)
#     j=lotto_bor.index(i)
#     del lotto_bor[j]
#     return i

# def main():
#     for i in range(5):
#         get_bor.append(lotto())
#     print(get_bor)
    

# main()
#####
import random as rnd

# def lotto():
#     numbers = rnd.sample(range(1, 50), 6)  # 隨機取6個不重複號碼
#     numbers.sort()
#     return numbers

# def main():
#     for i in range(5):
#         print(f"第 {i+1} 組號碼：", lotto())

# main()

def lotto():
    numbers=rnd.sample(range(1,50),6)
    numbers.sort()
    return numbers

def main():
    for i in range(5):
        print(f' {i}',lotto())
        
main()