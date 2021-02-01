liszt = []
while True:
    print('Enter list item or enter nothing to print list.')
    name = input()
    if name == '':
        break
    liszt = liszt + [name]
print('Your list is:')
if len(liszt) >= 3:
    for i in range(len(liszt) - 1):
        print((liszt[i]), end=', ')
    print('and ' + liszt[len(liszt) - 1])
elif len(liszt) == 2:
    print(liszt[0] + ' and ' + liszt[1])
elif len(liszt) == 1:
    print(liszt[0])
elif len(liszt) == 0:
    print('Your list is empty.')