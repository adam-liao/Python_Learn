# 4.	輸入數個整數儲存到集合，直到-9999結束，顯示這個集合的長度、最大值、最小值、總和。

S1=set()

while True:
    i=0
    i=int(input("Key In=>"))
    
    if i==-9999:
        break
    S1.add(i)

# S1=set(S1)
print(S1)
print(f'長度 {len(S1)} , 最大值 {max(S1)} , 最小值 {min(S1)} , 總合 {sum(S1)}')


    