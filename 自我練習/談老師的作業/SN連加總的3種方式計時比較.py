import time

N=10_000_000

start1=time.time()

s1=0
for i in range(1,N-1):
    s1+=1
end1 =time.time()
print(f' 方法1 用 for loop 總和={s1} 耗時{end1-start1:.6f}秒')

s2=0
start2=time.time()
s2=sum(range(1,N+1))
end2 =time.time()
print(f' 方法1 用 sum 總和={s2} 耗時{end2-start2:.6f}秒')

s3=0
start3=time.time()
s3=N*(N+1)//2
end3 =time.time()
print(f' 方法3 用 公式 總和={s3} 耗時{end3-start3:.6f}秒')

#用NumPy向量化計算
# import numpy as np
# S=np.sum(np.arange(1,N+1))
# print(S)