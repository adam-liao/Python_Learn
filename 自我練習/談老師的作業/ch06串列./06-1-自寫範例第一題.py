
import random as rnd
flig_index=['♣','♦','♥','♠'] 
index=[i+1 for i in range(13)]
print(index)

FC=index[:]
FC[0]="A"
FC[10]="J"
FC[11]="Q"
FC[12]="K"
print(FC)

def play_card():
    i=rnd.choice(FC)
    print("抽到",i)
    get_flower=rnd.choice(flig_index)
    return get_flower,i

def ddd(a,b,c,d):
    if FC.index(b)>FC.index(d) and flig_index.index(a) > flig_index.index(c):
        print(" YOU LOSE")
    else:
        print("YOU WIN")
        
        


a,b=play_card()
c,d=play_card()
print("computer ",a,b," Your",c,d)
ddd(a,b,c,d)