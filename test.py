price=int(input("ราคาสินค้าก่อนบวก Vat : "))
vat=7
result=price+(price*vat/100)
vats=(price*vat/100)
print("Vat : ",vats)
print("ราคาสินค้าหลังรวม Vat : ", result)