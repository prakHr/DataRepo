import json

def NumberInt(x):return int(x)
def NumberLong(x):return (0)

with open('f.json','r') as f:
    data=json.load(f)
myarray=data
#function calculates total Price from barcodePrice and gives missing barcodeStock as well 
totalPrice=0
for item in myarray:
    if len(item)==3:print("barcodeStock is missing /please check at "+str(item["barcodeNumber"]))
    totalPrice+=item.get("barcodePrice",0)
print("Number of barcodes/total bills in this kirana(+918008485850)=>"+str(len(myarray)))

print("Total Bill from this kirana=>"+str(totalPrice))
