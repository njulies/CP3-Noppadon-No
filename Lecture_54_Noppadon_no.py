def login():
    usernameinput=input("username : ")
    passwordinput=input("password : ")
    if usernameinput == "admin" and passwordinput == "1111":
        return showmenu()
    else:
        print("Wrong Username or Password")
        return login()
def showmenu():
    print("-----iShop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. จบโปรแกรม")
    return menuselect()
def menuselect():
    userselected = int(input("เลือกสินค้า"))
    if userselected==1:
        return vatcal()
    elif userselected==2:
        return pricecal()
    elif userselected==3:
        print("จบการทำงาน")
def vatcal():
    totalprice=int(input("ราคาสินค้าที่จะคำนวน THB :"))
    print("Vat มีราคาเท่ากับ : ",totalprice*0.07," THB")
    print("กลับไปเมนูสินค้า")
    return showmenu()
def pricecal():
    x=int(input("จำนวนสินค้า :"))
    z=0
    for i in range(x):
        print("ชิ้นที่",i+1)
        y=int(input("ราคาสินค้า :"))
        z=z+y
    print("ราคาสินค้าทั้งหมด",z," THB")
    return showmenu()
    #price1=int(input("First Product Price : "))
    #price2=int(input("Second Product Price : "))
    #print("ราคาสินค้าทั้งหมด",price1+price2," THB")
    #print("กลับไปเมนูสินค้า")
    #return showmenu()
login()