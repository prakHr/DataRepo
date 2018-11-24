'''
1. Make a main collection named anything(for ex,say Calculations)
2. (Run from terminal command line) python3.6 automateScript.py script1.py script2.py time-x time-y
3. where arguments are script1.py, script2.py,x sec,y sec to run corresponding scripts in x and y secs
   in sys.argv Array[]=[automateScript.py, script1.py, script2.py, time-x, time-y]
4. Store the address of main collection into variable (using path folder of scripts)
 '''
import os
import sys
from subprocess import *
import time

print('LENGTH OF LIST:',len(sys.argv))
print(sys.argv)
#python3.5 automationLinkedScript.py script1.py script2.py time-123 time-1223
script1=sys.argv[1]
script2=sys.argv[2]

scripts=[]
scripts.append(script1)
scripts.append(script2)

times=[]
t1=sys.argv[3];times.append(t1[5:])
t2=sys.argv[4];times.append(t2[5:])
print(times)
address='/home/zorro/Public/'
#scripts=['script1.py','script2.py']
for i in range(len(scripts)):
    time.sleep(int(times[i]))
    #os.system('python3.6 '+address+scripts[i])
    os.system('python3.6 '+scripts[i])
    
    

