
ListRow=2
ListColum=2
lst1=[]

listSum=list2=list1=[]

def type_list(lst,i_row,i_col):
    for i in range(i_row):
        lst.append([])
        for j in range(i_col):
            # lst[i].append(int(input("key in =>")))
            lst[i].append(j-i)

def dump_list(lst):
    for i in lst:
        print(i)

type_list(lst1,5,5)
dump_list(lst1)
