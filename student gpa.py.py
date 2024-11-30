total_vahed = 0 
Total_nomreh = 0  

while True:
    nomreh = float(input("لطفا نمره درس مئرد نظر را وارد کنید(براس خروج 0 را وارد کنید) "))
    if nomreh == 0:
        break
    
    vahed = int(input("لطفا تعداد واحد این درس را وارد کنید  "))
    while vahed <= 0:  
        print("واحد عددی مثبت و غیر صفر باید باشد")
        vahed = int(input("لطفا تعداد ئاحد این درس را وارد کنید "))

  
    if nomreh >= 10:
        total_vahed += vahed
        Total_nomreh += nomreh * vahed
    else:
        print("نمرات زیر 10 نادیده گرفته میشوند")
if total_vahed > 0:
    gpa = Total_nomreh / total_vahed
    print(f"معدل شما: {gpa:.2f}")
else:
    print("هیچ نمره مورد قبولی وارد نشد.")
