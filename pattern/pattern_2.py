num = int(input('Enter the number of rows: '))
k = 1
for r in range(1, num + 1):
    for j in range(1, k + 1):
        print('*', end='')
    k += 2
    print()
