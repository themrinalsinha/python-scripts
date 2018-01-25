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

