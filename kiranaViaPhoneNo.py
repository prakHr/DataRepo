import json
#function parses from json file 
#calculates total Price from barcodePrice ,
#gives missing barcodeStock as well ,only takes the barcodePrice<pow(10,criteria) in this case individualprice<10,000
def NumberInt(x):return int(x)
def NumberLong(x):return (0)

with open('f.json','r') as f:
    data=json.load(f)
myarray=data

totalPrice,criteria=0,4
for item in myarray:
    if len(item)==3:print("barcodeStock is missing /please check at "+str(item["barcodeNumber"]))
    if item["barcodePrice"]>=pow(10,criteria):
        print("item buyed with "+str(item["barcodeNumber"])+":"+str(item["barcodePrice"]))
        continue
    totalPrice+=item.get("barcodePrice",0)
print("Number of barcodes/total bills generated in this kirana(+91980258989)=>"+str(len(myarray)))

print("Total Bill from this kirana=>"+str(totalPrice))
