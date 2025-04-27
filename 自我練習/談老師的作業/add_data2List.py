names={'bob':50,'anna':30,'adam':40,'julia':90,'lydia':70}

# for name in names:
#     while True:
#         try:
#             score=int(input(f" {name} Input score =>"))
#             if 0<= score  <=100:
#                 names[name]=score
#                 break
#             else:
#                 print("range is 0-100")
#         except:
#             print("請輸入總數")
#         else:
#             print("再重新輸入一次")

# for name,score in sorted(names.items(),key=lambda item:item[1]):
#     print(f'{name} = {score}')

report_a=sorted(names.items(),key=lambda x:x[1],reverse=True)
for i,name in enumerate(report_a,1):
    print(f'{i} {name}')