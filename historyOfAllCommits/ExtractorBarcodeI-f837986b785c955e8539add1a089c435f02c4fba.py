import firebase_admin
from firebase_admin import *
from firebase_admin import firestore
import time
from datetime import timedelta

cred1=credentials.Certificate("munshik3-46360-firebase-adminsdk-d1ymf-4358fc0962.json")

#function takes the credentials(=>input) and gives reference address to database(=>db)
def extractDatabase(cred):
    app=firebase_admin.initialize_app(cred)
    db=firestore.client()
    delete_app(app)
    return db

db1=extractDatabase(cred1)

barcode_inventory_docs=db1.collection(u'barcode_inventory').get()
barcode_inventory_ref=db1.collection(u'barcode_inventory')

#for loop takes distinct barcodes using lower method of string in a set
barcodes_set,barcodes_array=set(),[]
first_two_digit_barcodes_array=[]

#for loop takes first 2 digits of barcodes in an array(not set to use for count),and a array of barcodes for similar purpose 
for doc in barcode_inventory_docs:
    b=doc.id
    b=b.lower()
    barcodes_set.add(b)
    first_two_digit_barcodes_array.append(b[0:2])
    barcodes_array.append(b)

#for loop takes all the possible lengths of barcodes in a set(surprised this set could have any possible permutation but it gave increasing order of lengths)
barcodes_len_set=set()
for b in barcodes_set:
    barcodes_len_set.add(len(b))
#print('barcodes_len_set=>',barcodes_len_set)

#for loop counts the number of barcodes using its length
for l in barcodes_len_set:
    count=0
    for b in barcodes_array:
        if len(b)==l:
            count+=1
    #print('length of barcode',l,'total :',count)

#for loops keeps barcodes with first 2 and last 2 same digits into an arraySet=>(DoubleDigit,len(corresponding_barcode))
sameLastTwoDigitArraySet,sameFirstTwoDigitArraySet,countOfSameFirstTwoDigit=set(),set(),0
for b in barcodes_array:
    if b[0]==b[1]:
        countOfSameFirstTwoDigit+=1

for b in barcodes_set:
    if b[0]==b[1]:
        sameFirstTwoDigitArraySet.add((b[0]*2,len(b)))
    if b[-1]==b[-2]:
        sameLastTwoDigitArraySet.add((b[-1]*2,len(b)))

#print('countOfSameFirstTwoDigit :-',countOfSameFirstTwoDigit)

sameFirstTwoDigit=set()

#same first 2 digits are taken into array from array set
sameFirstTwoDigitArray=set()
for (a,b) in sameFirstTwoDigitArraySet:
    sameFirstTwoDigitArray.add(a)

#print('sameFirstTwoDigitArray=>',sameFirstTwoDigitArray)
CountsOfSameTwoDigit=[]

for a in sameFirstTwoDigitArray:
    count=0
    for b in barcodes_array:
        if a==b[0:2]:
            count+=1
    CountsOfSameTwoDigit.append([count,a])

#print('CountsOfSameTwoDigit=>',CountsOfSameTwoDigit)

#function takes database(optional args, not necessary) and reference of main collection as input and then gives an array of [[barcodeNumber1,lower(barcodeName1),barcodePrice1],...]
#other outputs are :-a price dictionary of key-value pair as {(barcodeNumber1,lower(barcodePrice1)),(barcodeNumber2,lower(barcodePrice2))..}, a name dictionary of key-value pair as {(barcodeNumber1,lower(barcodeName1)),(barcodeNumber2,lower(barcodeName2))...}
def extractNameAndPriceFromBarcodes(database,reference):
    array=[]
    price_dict,name_dict={},{}
    docs=reference.get()
    for doc in docs:
        ids,my_dict=doc.id,doc.to_dict()
        number,name,price=my_dict['barcodeNumber'],my_dict['barcodeName'].lower(),my_dict['barcodePrice']
        name=name.replace(" ","")
        array.append([number,name,price])
        key=number
        price_dict[key]=price
        name_dict[key]=name
    return array,price_dict,name_dict


barcodesArray,barcodesPriceDict,barcodesNameDict=extractNameAndPriceFromBarcodes(db1,barcode_inventory_ref)
#print('barcodesPriceDict=>',barcodesPriceDict)
#print('barcodesNameDict=>',barcodesNameDict)

#function takes digits,(digits+1),barcodesSet,price dictionary,name dictionary(where digits come from an array in the for loop) and output is 2 sets that takes barcodes of corresponding lengths(digits,digits+1) and becomes an input for subfunction
#function also contains a sub function that takes 2 sets and a dictionary as input and gives output in array of the form [count,Dict[key1],a,b] iff a=b where a=Dict[digits],b=Dict[digits+1]
#so according to nature of dictionaries(name/Price) Dict[digits]=name/Price which gives similarity
#output is gonna be 2 arrays that contains barcodes in the format [count,sameValue(either price/name),barcode1(of len digits),barcode2(of len digits-1)]
def similarity(bLen_minus_one_digit,bLen_digit,barcodes,priceDict,nameDict,switchCase):
    bLen_minus_one_digit_set,bLen_digit_set=set(),set()
    for b in barcodes:
        if len(b)==bLen_minus_one_digit:
            bLen_minus_one_digit_set.add(b)
        if len(b)==bLen_digit:
            bLen_digit_set.add(b)
            
    #number of substrings in which both barcodeNames and barcodePrices are different
    def function4(set1,set2,Dict1,Dict2):#set theory is not valid here, i.e. to count not intersection a+b-2*(a Intersect b)
        Array=[]
        for a in set1:
            count,flag=0,False
            if a not in Dict1:continue
            if a not in Dict2:continue
            for b in set2:
                if b not in Dict1:continue
                if b not in Dict2:continue
                #need to uncomment for 2 digit difference
                #if (b==a[:-2] or b==a[2:]):flag=True
                if (b==a[:-1] or b==a[1:]):
                    flag=True
                if Dict1[a]!=Dict1[b] and Dict2[a]!=Dict2[b]:
                    if flag==True:
                        Array.append([Dict1[a],Dict1[b],Dict2[a],Dict2[b],a,b])#flag comes True is showing correctly
                    flag=False
                flag=False
        return Array

    #number of substrings in which only barcodeNames are same
    def function3(set1,set2,Dict1,Dict2):
        Array=[]
        for a in set1:
            count,flag=0,False
            if a not in Dict1:continue
            if a not in Dict2:continue
            for b in set2:
                if b not in Dict1:continue
                if b not in Dict2:continue
                #if (b==a[:-2] or b==a[2:]):flag=True
                if (b==a[:-1] or b==a[1:]):flag=True
                if Dict1[a]!=Dict1[b] and Dict2[a]==Dict2[b]:
                    if flag==True:
                        Array.append([Dict1[a],Dict1[b],Dict2[a],Dict2[b],a,b])
                    flag=False
                flag=False
        return Array

    #number of substrings in which only barcodesPrices are same
    def function2(set1,set2,Dict1,Dict2):
        Array=[]
        for a in set1:
            count,flag=0,False
            if a not in Dict1:continue
            if a not in Dict2:continue
            for b in set2:
                if b not in Dict1:continue
                if b not in Dict2:continue
                #if (b==a[:-2] or b==a[2:]):flag=True
                if (b==a[:-1] or b==a[1:]):flag=True
                if Dict1[a]==Dict1[b] and Dict2[a]!=Dict2[b]:
                    if flag==True:
                        Array.append([Dict1[a],Dict1[b],Dict2[a],Dict2[b],a,b])
                    flag=False
                flag=False
        return Array

    #number of substrings in which both barcodesPrices and barcodeNames are same
    def function1(set1,set2,Dict1,Dict2):
        Array=[]
        for a in set1:
            count,flag=0,False
            if a not in Dict1:continue
            if a not in Dict2:continue
            for b in set2:
                if b not in Dict1:continue
                if b not in Dict2:continue
                #if (b==a[:-2] or b==a[2:]):flag=True
                if (b==a[:-1] or b==a[1:]):flag=True
                if Dict1[a]==Dict1[b] and Dict2[a]==Dict2[b]:
                    if flag==True:
                        Array.append([Dict1[a],Dict1[b],Dict2[a],Dict2[b],a,b])
                    flag=False
                flag=False
        return Array

    #number of substrings in which either of prices or names are same in accordance to dictionary, i.e. ,priceDict or nameDict
    def function(set1,set2,Dict):
        Array=[]
        for a in set1:
            count,flag=0,False
            if a not in Dict:continue
            for b in set2:
                if b not in Dict:continue
                #if (b==a[:-2] or b==a[2:]):flag=True
                if (b==a[:-1] or b==a[1:]):
                    flag=True
                if Dict[a]==Dict[b]:
                    if flag==True:
                        Array.append([Dict[a],a,b])
                    flag=False
                flag=False
        return Array

    #according to switchCases corresponding sub functions are called in similarity, for example ,function 1,2,3,4
    set1,set2=bLen_minus_one_digit_set,bLen_digit_set
    if switchCase==0:
        CountArrayForPrices,CountArrayForNames=function(set1,set2,priceDict),function(set1,set2,nameDict)
        return CountArrayForPrices,CountArrayForNames
    elif switchCase==1:
        CountArrayForPricesAndNames=function1(set1,set2,priceDict,nameDict)
        return CountArrayForPricesAndNames
    elif switchCase==2:
        CountArrayForPricesAndNames=function2(set1,set2,priceDict,nameDict)
        return CountArrayForPricesAndNames
    elif switchCase==3:
        CountArrayForPricesAndNames=function3(set1,set2,priceDict,nameDict)
        return CountArrayForPricesAndNames
    elif switchCase==4:
        CountArrayForPricesAndNames=function4(set1,set2,priceDict,nameDict)
        return CountArrayForPricesAndNames

#to run function for digits with difference 2
x_minus_one_digit_array=[3,4,5,6,7,8,9,10,11,12,13,14,15]
second_digits_array=[(12,14),(11,13),(10,12),(13,15),(14,16)]
cases=[1,2,3]
numberZero,numberFour=0,4
print('----------------------------------------------------')
def PrintTwoDifferenceArrayForfunction(second_digits_array,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase):
    for (a1,b1) in second_digits_array:
        array1,array2=similarity(a1,b1,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase)
        count=0
        for a in array1:
            print(a[0],',',a[1],',',a[2])
            count+=1
        #print('count of substring similarity of barcode for digit ',a1,' with digit ',b1,' is ',count)
        #print('Length of CountArray for Prices is ',len(array1),' with ',a1,' & ',b1,' digit')
        count=0
        for a in array2:
            print(a[0],',',a[1],',',a[2])
            count+=1
        #print('count of substring similarity of barcode for digit ',a1,' with digit ',b1,' is ',count)
        #print('Length of CountArray for Prices is ',len(array1),' with ',a1,' & ',b1,' digit')
        #print('-------------------------------------------------------------')
print('Here')
PrintTwoDifferenceArrayForfunction(second_digits_array,barcodes_set,barcodesPriceDict,barcodesNameDict,numberZero)

#to run function for digits with difference 1
def PrintOneDifferenceArrayForfunction(x_minus_one_digit_array,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase):
    for digit in x_minus_one_digit_array:
        x_digit=digit+1
        x_minus_one_digit=digit
        array1,array2=similarity(x_digit,x_minus_one_digit,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase)
        count=0
        for a in array1:
            print(a[0],',',a[1],',',a[2])
            count+=1
        #print('count of substring similarity of barcode for digit ',x_digit,' with digit ',x_minus_one_digit,' is ',count)
        #print('Length of CountArray for Prices is ',len(array1),' with ',x_digit,' & ',x_minus_one_digit,' digit')
        count=0
        for a in array1:
            print(a[0],',',a[1],',',a[2])
            count+=1
        #print('Length of CountArray for Prices is ',len(array1),' with ',x_digit,' & ',x_minus_one_digit,' digit')
        #print('-------------------------------------------------------------')
print('Here')
PrintOneDifferenceArrayForfunction(x_minus_one_digit_array,barcodes_set,barcodesPriceDict,barcodesNameDict,numberZero)

#to run function1, function2, function3 for digits with difference 2
def PrintTwoDifferenceArrayForfunction_1_2_3(second_digits_array,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase):
    for (a1,b1) in second_digits_array:
        array1=similarity(a1,b1,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase)
        count=0
        for a in array1:
            print(a[0],',',a[1],',',a[2],',',a[3],',',a[4],',',a[5])
            count+=1
        #print('count of substring similarity of barcode for digit ',a1,' with digit ',b1,' is ',count)
        #print('Length of CountArray for Prices is ',len(array1),' with ',a1,' & ',b1,' digit')

for c in cases:
    print('Here')
    PrintTwoDifferenceArrayForfunction_1_2_3(second_digits_array,barcodes_set,barcodesPriceDict,barcodesNameDict,c)

#to run function1, function2, function3 for digits with difference 1
def PrintOneDifferenceArrayForfunction_1_2_3(x_minus_one_digit_array,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase):
    for digit in x_minus_one_digit_array:
        x_digit=digit+1
        x_minus_one_digit=digit
        array1=similarity(x_digit,x_minus_one_digit,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase)
        count=0
        for a in array1:
            print(a[0],',',a[1],',',a[2],',',a[3],',',a[4],',',a[5])
            count+=1
        #print('count of substring similarity of barcode for digit ',x_digit,' with digit ',x_minus_one_digit,' is ',count)
        #print('Length of CountArray for Prices is ',len(array1),' with ',x_digit,' & ',x_minus_one_digit,' digit')

for c in cases:
    print('Here')
    PrintOneDifferenceArrayForfunction_1_2_3(x_minus_one_digit_array,barcodes_set,barcodesPriceDict,barcodesNameDict,c)
    
#to run function4 for digits with difference 1
def PrintOneDifferenceArrayForfunction_4(x_minus_one_digit_array,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase):
    for digit in x_minus_one_digit_array:
        x_digit=digit+1
        x_minus_one_digit=digit
        array1=similarity(x_digit,x_minus_one_digit,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase)
        count=0
        for a in array1:
            print(a[0],',',a[1],',',a[2],',',a[3],',',a[4],',',a[5])
            count+=1
        #print('count of substring similarity of barcode for digit ',x_digit,' with digit ',x_minus_one_digit,' is ',count)
        #print('Length of CountArray for Prices is ',len(array1),' with ',x_digit,' & ',x_minus_one_digit,' digit')

PrintOneDifferenceArrayForfunction_4(x_minus_one_digit_array,barcodes_set,barcodesPriceDict,barcodesNameDict,numberFour)

#to run function4 for digits with difference 2
def PrintTwoDifferenceArrayForfunction_4(second_digits_array,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase):
    for (a1,b1) in second_digits_array:
        array1=similarity(a1,b1,barcodes_set,barcodesPriceDict,barcodesNameDict,switchCase)
        count=0
        for a in array1:
            print(a[0],',',a[1],',',a[2],',',a[3],',',a[4],',',a[5])
            count+=1
        #print('count of substring similarity of barcode for digit ',a1,' with digit ',b1,' is ',count)
        #print('Length of CountArray for Prices is ',len(array1),' with ',a1,' & ',b1,' digit')
print('Here')
PrintTwoDifferenceArrayForfunction_4(second_digits_array,barcodes_set,barcodesPriceDict,barcodesNameDict,numberFour)
