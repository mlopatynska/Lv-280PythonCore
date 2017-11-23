num=[2,4,7,1,6,5,6]
min_el=num[0]
i=0
while i <len(num):
    if min_el>num[i]:
        min_el=num[i]
    i += 1
print min_el