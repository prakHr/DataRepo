def NumberInt(n):return int(n)
def NumberLong(n):return int(n)
import json

#barcodes comes from barcodeInventory
setToBeSearched=set()
namesToBeSearched=set()
#counter=0
with open('f2.json' ,'rt', encoding='utf-8') as f:
    data=json.load(f)
  #  counter+=1
for key in data:
    setToBeSearched.add(key)

    
#print(counter)
#for barcode in arrayToBeSearched:

with open('f.json','r') as f:
    data=json.load(f)
myarray=data                 
myarraySet=set()
barcodeNames=[]
for item in myarray:
    myarraySet.add(item["barcodeNumber"])
    barcodeNames.append(item["barcodeName"])
    
a=(len(myarraySet))
b=(len(setToBeSearched))#len of barcodeInventory
c=(myarraySet & setToBeSearched)#common barcodes in kirana Phone and barcode Inventory

barcodeItems=[]
for barcodes in c:
    print(barcodes)
print("This Kirana uses these many barcodes from barcodeInventory=>"+str(len(c)))

#function searches for barcodeNames in kirana Phone array using set(c)
for barcodes in c:
    for items in myarray:
        if items["barcodeNumber"]==barcodes:
            barcodeItems.append(items["barcodeName"])
print("This Kirana uses this many items from barcodeInventory=>")
print(barcodeItems)
print(len(barcodeItems))#gives length of barcodeItems that is present in barcodeInventory    

#is Particular kirana ke paas ye waale barcodes hai but agar 100 kiranas hoge toh
  
