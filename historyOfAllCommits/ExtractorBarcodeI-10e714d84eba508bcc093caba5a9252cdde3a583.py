import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
from datetime import timedelta

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")

def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db1=extractDatabase(cred1)

barcode_inventory_docs=db1.collection(u'barcode_inventory').get()
barcode_inventory_ref=db1.collection(u'barcode_inventory')

barcodes_set=set()
for doc in barcode_inventory_docs:
    #print(doc.id)
    barcodes_set.add(doc.id)

barcodes_len_set=set()
for b in barcodes_set:
    barcodes_len_set.add(len(b))
#print(barcodes_len_set)#{3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20}

for l in barcodes_len_set:
    count=0
    for b in barcodes_set:
        if len(b)==l:
            count+=1
    #print(l,count)
    #3 1
    #4 1
    #5 1
    #6 3
    #7 10
    #8 111
    #9 8
    #10 13
    #11 31
    #12 316
    #13 9434
    #14 58
    #15 4
    #16 2
    #20 1

sameLastTwoDigitArraySet,sameFirstTwoDigitArraySet=set(),set()
for b in barcodes_set:
    if b[0]==b[1]:
        sameFirstTwoDigitArraySet.add((b[0]*2,len(b)))
    if b[-1]==b[-2]:
        sameLastTwoDigitArraySet.add((b[-1]*2,len(b)))
#print('sameLastTwoDigitArraySet=>',sameLastTwoDigitArraySet)
#{('00', 12), ('11', 13), ('hh', 3), ('00', 8), ('00', 13), ('33', 8), ('00', 9), ('99', 12), ('33', 12), ('88', 12), ('55', 13), ('11', 11), ('77', 13), ('66', 13), ('22', 8), ('99', 13), ('44', 8), ('33', 13), ('88', 13), ('22', 12), ('44', 12), ('55', 12), ('11', 8), ('99', 10), ('77', 12), ('55', 8), ('11', 12), ('33', 10), ('77', 8), ('22', 13), ('00', 11), ('44', 13), ('33', 14), ('88', 14)}
sameFirstTwoDigit=set()
#print('sameFirstTwoDigitArraySet=>',sameFirstTwoDigitArraySet)
#{('66', 11), ('88', 10), ('88', 14), ('77', 12), ('00', 12), ('99', 12), ('44', 14), ('88', 13), ('99', 13), ('88', 12), ('11', 4), ('77', 13), ('66', 14)}
def extractNameAndPriceFromBarcodes(database,reference):
    array=[]
    price_dict,name_dict={},{}
    docs=reference.get()
    for doc in docs:
        ids,my_dict=doc.id,doc.to_dict()
        number,name,price=my_dict['barcodeNumber'],my_dict['barcodeName'],my_dict['barcodePrice']
        array.append([number,name,price])
        key=number
        price_dict[key]=price
        name_dict[key]=name
    return array,price_dict,name_dict


barcodesArray,barcodesPriceDict,barcodesNameDict=extractNameAndPriceFromBarcodes(db1,barcode_inventory_ref)
#print('barcodesPriceDict=>',barcodesPriceDict)
#print('barcodesNameDict=>',barcodesNameDict)

def TwoSameNames(arraySet):
    s=set()
    for (a,b) in arraySet:
        s.add(a)
    return s

sameFirstTwoDigit,sameLastTwoDigit=TwoSameNames(sameFirstTwoDigitArraySet),TwoSameNames(sameLastTwoDigitArraySet)

def distinctDoubleDigits(arrayContainingSameDigits,arraySet):
    g=0
    DOUBLE_DIGITS=[]
    for double_digits in arrayContainingSameDigits:
        previous_g=0
        for (a,b) in arraySet:
            if double_digits==a:
                g=max(b,g)
        DOUBLE_DIGITS.append([double_digits,g])
        g=0
    return DOUBLE_DIGITS

SameDoubleDigits1=distinctDoubleDigits(sameFirstTwoDigit,sameFirstTwoDigitArraySet)
#print(SameDoubleDigits1)
#[['88', 14], ['00', 12], ['66', 14], ['99', 13], ['11', 4], ['77', 13]]
SameDoubleDigits2=distinctDoubleDigits(sameLastTwoDigit,sameLastTwoDigitArraySet)
#print(SameDoubleDigits2)
#[['44', 13], ['22', 13], ['hh', 3], ['77', 13], ['33', 14], ['99', 13], ['88', 14], ['55', 13], ['11', 13], ['66', 13], ['00', 13]]

def similarity(bLen_minus_one_digit,bLen_digit,barcodes,priceDict,nameDict):
    bLen_minus_one_digit_set,bLen_digit_set=set(),set()
    for b in barcodes:
        if len(b)==bLen_minus_one_digit:
            bLen_minus_one_digit_set.add(b)    
        if len(b)==bLen_digit:
            bLen_digit_set.add(b)
    
    def function(set1,set2,Dict):
        Array=[]
        for a in set1:
            count=1
            if a not in Dict:continue
            for b in set2:
                if a not in Dict:continue
                if b not in Dict:continue
                if b in set1 and Dict[a]==Dict[b]:
                    count+=1
            Array.append([count,Dict[a],a,b])
        return Array
    
    set1,set2=bLen_minus_one_digit_set,bLen_digit_set
    CountArrayForPrices,CountArrayForNames=function(set1,set2,priceDict),function(set1,set2,nameDict)
    '''
    CountArrayForPrices,CountArrayForNames=[],[]
    for b_minus_one in bLen_minus_one_digit_set:
        count=1
        if b_minus_one not in priceDict:continue
        for b_one in bLen_digit_set:#need to add visited as a data structure as well
            if b_one not in priceDict:continue
            if b_minus_one not in priceDict:continue
            if priceDict[b_minus_one] ==priceDict[b_one]:
                count+=1
        CountArrayForPrices.append([count,priceDict[b_minus_one],b_minus_one,b_one])

    for b_minus_one in bLen_minus_one_digit_set:
        count=1
        if b_minus_one not in nameDict:continue
        for b_one in bLen_digit_set:
            if b_one not in nameDict:continue
            if b_minus_one not in nameDict:continue
            if nameDict[b_minus_one] ==nameDict[b_one]:
                count+=1
        CountArrayForNames.append([count,nameDict[b_minus_one],b_minus_one,b_one])
        '''
    return CountArrayForPrices,CountArrayForNames
    
x_minus_one_digit=[3,4,5,6,7,8,9,10,11,12,13,14,15]

for digit in x_minus_one_digit:
    x_digit=digit+1
    x_minus_one_digit=digit
    array1,array2=similarity(x_digit,x_minus_one_digit,barcodes_set,barcodesPriceDict,barcodesNameDict)
    #print(array1,array2)
    for a in array1:
        print(a,end='\n')
    for a in array2:
        print(a,end='\n')
    











