user_id="adam"
password="1234"

id_error_count=0
password_error_count=0

while True:
    try:
        input_id=input(">請輸入帳號 ")
    except:
        print(" 輸入錯誤，請再試一次")
        continue #回到 while
    
    if input_id != user_id:
        id_error_count+=1
        print(f'帳號輸入錯誤 {id_error_count}次')
        if id_error_count>=3:
          print('帳號錯誤超過3次')
          break
        continue #回到 while
    else:
        print('帳號正確')
    
    while password_error_count < 3:
        try:
            input_pw=input("請輸入密碼 ")
        except:
            print('密碼輸入錯誤')
            continue
        
        if password!=input_pw:
            password_error_count+=1
            print(f'密碼輸入錯誤 {password_error_count}次')
            if(password_error_count>=3):
                print('密碼輸入錯誤，超過3次')
                break
            continue
        else:
          print('密碼正確，登入成功')
          break
    break

print('end')
        