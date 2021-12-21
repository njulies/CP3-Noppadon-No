total=int(input("ราคาก่อนคำนวนภาษี :"))
def vatcal(total):
    result=(total*1.07)
    return result           # return result กลับไปแทนที่ total
print(vatcal(100))
