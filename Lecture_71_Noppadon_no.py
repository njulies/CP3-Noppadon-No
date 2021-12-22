menulist=[]
pricelist=[]
def showbill():
    sum=0
    for i in range(len(menulist)):
        print("menu :",menulist[i],"price :",pricelist[i])
        sum+=pricelist[i]
    print("รวมราคา :",sum)
while True:
    menuname=input("Please Enter menu : ")
    if menuname.lower() == "exit":
        break
    else:
        menuprice=int(input("Please Enter Price : "))
        menulist.append(menuname)
        pricelist.append(menuprice)
showbill()