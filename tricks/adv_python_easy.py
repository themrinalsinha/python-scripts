# list comprehension
# ---> Segregate positive and negative numbers in an array

def segregate(arr):
    return [x for x in arr if x%2 == 0] + [x for x in arr if x%2 != 0]
arr = list(range(1, 10))
arr = segregate(arr)
print(arr)


