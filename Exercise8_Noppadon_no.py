user = input("username : ")
pas = input("password : ")
if user == "wick" and pas == "1111":
    print("Welcome to Fruity Shop\n1.Apple : 10 $\n2.Banana : 5 $\n3.Orange : 15 $")
    p1=10
    p2=5
    p3=15
    n1 = int(input("Apple จำนวน(ลูก) :"))
    n2 = int(input("Banana จำนวน(ลูก) :"))
    n3 = int(input("Orange จำนวน(ลูก) :"))
    print("ราคา Apple :", n1*p1)
    print("ราคา Banana :", n2 *p2)
    print("ราคา Orange :", n3 * p3)
    print("รวมราคาสินค้า :", (n1*p1)+(n2*p2)+(n3*p3), "$")
    vat=((n1 * p1) + (n2 * p2) + (n3 * p3))*7/100
    print("Vat+7%",vat)
    print("รวมราคาสินค้าบวกVat :", ((n1 * p1) + (n2 * p2) + (n3 * p3))+vat, "$")
print("*****Thank you*****")