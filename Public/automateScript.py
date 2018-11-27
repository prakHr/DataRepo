'''
1. Make a main collection named anything(for ex,say Calculations)
2. (Run from terminal command line) python3.6 automateScript.py script1.py script2.py time-x time-y
3. where arguments are script1.py, script2.py,x sec,y sec to run corresponding scripts in x secs
   in sys.argv Array[]=[automateScript.py, script1.py, script2.py,script3.py,script4.py, time-x]
4. Store the address of main collection into variable (using path folder of scripts)
 '''
import os
import sys
from subprocess import *
import time
import decimal

def fileReader(text_file):
    file1=open(text_file,"r+")
    timeValue=file1.read()
    time_string=timeValue.strip('\n')
    temp=decimal.Decimal(time_string)
    return float(temp)

'''
print('LENGTH OF LIST:',len(sys.argv))
print(sys.argv)
'''

#python3.5 automationLinkedScript.py script1.py script2.py script3.py script4.py time-12

script1=sys.argv[1]
script2=sys.argv[2]
script3=sys.argv[3]
script4=sys.argv[4]

scripts=[]
scripts.append(script1)
scripts.append(script2)
scripts.append(script3)
scripts.append(script4)

'''
test_scripts=[]
test_scripts.append(script1)
test_scripts.append(script2)
'''
times=sys.argv[5]

print(times)

address='/home/zorro/Public/'
#scripts=['script1.py','script2.py']
for i in range(len(scripts)):
    time.sleep(1)
    #os.system('python3.6'+blankSpace+address+scripts[i]+blankSpace+'>'+blankSpace+'time_script.txt')
    os.system('python3.6 '+scripts[i]+' > '+'time_script'+str(i)+'.txt')
    time.sleep(2)
    tmp=fileReader('time_script'+str(i)+'.txt')
    time.sleep(tmp)
    time.sleep(int(times))
   

'''
for i in range(len(test_scripts)):
    time.sleep(1)
    os.system('python3.6 '+test_scripts[i]+' > '+'time_script'+str(i)+'.txt')
    time.sleep(2)
    tmp=fileReader('time_script'+str(i)+'.txt')
    time.sleep(tmp+10)
'''   
