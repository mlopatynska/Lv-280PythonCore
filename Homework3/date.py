a = input('Enter year\n')
if a < 0:
    print('Incorrect data')
else:
    b = input('Enter month\n')
    if b not in range(1,13):
        print('Incorrect data of month')
    else:
        c = input('Enter day\n')
        if c not in range(1,32):
            print('Incorrect data of day')
        else:
            print ('Year =', a, 'Month =', b, 'Day =', c)

