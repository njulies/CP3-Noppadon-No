systemmenu={"a":50,"b":45,"c":60,"d":75}
menulist=[]
def showbill():
    sum=0
    for i in range(len(menulist)):
        print("menu :",menulist[i][0],"Price :",menulist[i][1],"THB")
        sum+=menulist[i][1]
    print("Total Price :",sum,"THB")
for k,v in systemmenu.items():
    print("menu :",k,"Price :",v,"THB")
while True:
    menuname=input("Please Enter menu : ")
    if menuname.lower() == "exit":
        break
    else:
        menulist.append([menuname,systemmenu[menuname]])
showbill()