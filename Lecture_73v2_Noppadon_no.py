systemmenu={"a":50,"b":45,"c":60,"d":75}
menulist=[]
sum=0
def showbill():
    for i in range(len(menulist)):
        print("menu :",menulist[i][0],"Price :",menulist[i][1],"THB")
    print("Total Price :",sum,"THB")
for k,v in systemmenu.items():
     print("menu :",k,"Price :",v,"THB")
while True:
    menuname=input("Please Enter menu : ")
    if menuname.lower() == "exit":
        break
    else:
        menulist.append([menuname,systemmenu[menuname]])
        sum+=systemmenu[menuname]
        print(sum)
showbill()