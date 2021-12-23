menulist=[]
def showbill():
    sum=0
    for i in range(len(menulist)):
        print("menu :",menulist[i][0],"Price :",menulist[i][1],"THB")
        sum+=menulist[i][1]
    print("Total Price :",sum,"THB")
while True:
    menuname=input("Please Enter menu : ")
    if menuname.lower() == "exit":
        break
    else:
        menuprice=int(input("Please Enter Price : "))
        menulist.append([menuname,menuprice])
showbill()