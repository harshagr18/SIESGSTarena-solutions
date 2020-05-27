x = int(input())
for i in range(x):
    a = int(input())
    a = a*2 - (0.2 * a)
    print('%.2f'%a)