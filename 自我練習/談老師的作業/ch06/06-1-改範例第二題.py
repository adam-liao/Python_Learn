item=["姓名","國文","數學","英文"]


def compute(name):
    score=["",0,0,0]
    score[0]=name
    tol=0
    for i in range(1,len(item)):
        score[i]=int(input(f' {item[i]}'))
    
    print('各科成績',*score[1:])
    print()
    for i in range(1,len(score)):
        # print(score[i])
        tol+=score[i]
    print(f'總分 {tol} 平均{tol/i:5.1f}')
    print()
 

def main():
    while True:
        name=input("input a name ")
        if name=="":
            break
        else:
            compute(name)

main()
        