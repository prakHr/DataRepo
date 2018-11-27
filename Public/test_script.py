import time
start_time=time.time()
def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

end_time=time.time()-start_time
x=fibonacci(20)
#print('fibonacci(20)=>',x)
#1 1 2 3 5 8 13 21 34 55 89
print(end_time)


