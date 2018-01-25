# Multiprocessing pool

def f(n):
    return n * n

if __name__ == '__main__':
    array = [2,5,6,7,8,3]

    result = []
    for n in array:
        result.append(f(n))

    print(result)

# Generally, the function loads the above function in a any of core and process the input and rest all the cores are sitting idle.

# Now if somehow if you can deploy your code on all the cores and divide you input between all the cores and then after processing aggregate all the results together
# Parallel processing.
# Map --- Distributing input to multiple cores is called map.
# Reduce -- Aggregiating all the processes results together is call reduce.

print("\n------------MULTIPROCESSING-----------\n")

from multiprocessing import Pool
import time

def f2(n):
    sum = 0
    for x in range(100):
        sum += x * x
    return sum

t1 = time.time()
p = Pool()
result = p.map(f2, range(1000000))
p.close()
p.join()
print("POOL TOOK : {}".format(time.time() - t1))

t2 = time.time()
res = []
for x in range(1000000):
    result.append(f2(x))

print('Serial processing took : {}'.format(time.time() - t2))

# When you want to limit the number of pools you can do that
# p = Pool(processes = 3)