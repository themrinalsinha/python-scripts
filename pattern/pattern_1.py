# Pattern program...

num = int(input('Enter number of rows: '))
for r in range(1, num + 1):
    for c in range(1, r + 1):
        print('*', end=' ')
    print()
