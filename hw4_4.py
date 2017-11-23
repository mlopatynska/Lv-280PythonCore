x=input('Enter =')

x=str(x)
S=0
for i in range(len(x)):
    S+=int(x[i])**3
print ('Suma = {}').format(S)
