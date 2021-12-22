menulist=[]
pricelist=[]
def showbill():
    total=0
    for i in range(len(menulist)):
        print("menu :",menulist[i],"price :",pricelist[i])
        total+=pricelist[i]
    print("Total Price :",total,"THB")
while True:
    menuname=input("Please Enter menu : ")
    if menuname.lower() == "exit":
        break
    else:
        menuprice=int(input("Please Enter Price : "))
        menulist.append(menuname)
        pricelist.append(menuprice)
showbill()