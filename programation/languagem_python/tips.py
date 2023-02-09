# Use Type Hints
## https://www.pythontutorial.net/python-basics/python-type-hints/
# Organize your importations https://marketplace.visualstudio.com/items?itemName=ms-python.isort
# Run codes more fast
## Low--------
import time

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'
    
starttime = time.time()
for i in range(0,10):
    y = i*i
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(i, basic_func(y)))
    
print('That took {} seconds'.format(time.time() - starttime))
# Fast--------
import time
import multiprocessing 

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    y = x*x
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(0,10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print('That took {} seconds'.format(time.time() - starttime))

==========================================================================
# Run loops for more fast
def sum_1(a:int):
    return a+1

import joblib
import time
start_time = time.time()
num = 10000
with joblib.parallel_backend("loky"):
    with joblib.Parallel() as parallel:
        print("Doing the work ... ")
        results = parallel(joblib.delayed(sum_1)(s) for s in range(num))

# print(results)
print(time.time()-start_time)
start_time = time.time()
with joblib.parallel_backend('threading'):
    with joblib.Parallel() as parallel:
        print("Doing the work ... ")
        results = parallel(joblib.delayed(sum_1)(s) for s in range(num))
print(time.time()-start_time)
print(time.time()-start_time)
start_time = time.time()
with joblib.parallel_backend('multiprocessing'):
    with joblib.Parallel() as parallel:
        print("Doing the work ... ")
        results = parallel(joblib.delayed(sum_1)(s) for s in range(num))
print(time.time()-start_time)
    
