# 5.	依序輸入五個、三個、九個整數，儲存到set1、set2、set3當中，查詢set2是否為set1的子集合?set3是否為set1的超集合?

S1,S2,S3=[set() for _ in range(3)]
# S1=set();S2=set();S3=set()

def keyinNumber(SS,j):
    print(f'請輸入{j}個數值,輸入重覆會被捨棄')
    while len(SS)<j:
        i=0
        i=int(input("key in => "))
        SS.add(i)
   
   
keyinNumber(S1,5)
keyinNumber(S2,3)
keyinNumber(S3,9)
print(S1)
print(S2)
print(S3)

a=S2.issubset(S1)
b=S3.issuperset(S1)

print(a,b)
