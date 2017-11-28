import random
Matrix = [[random.randint(1, 100) for x in range(5)] for y in range(5)]
list_index_max_values_matr=[]
max_matr=[]   
for i in Matrix:
    max_matr.append(max(i))
    list_index_max_values_matr.append(i.index(max(i)))
coordin_max_val=[]
coordin_max_val.append(max_matr.index(max(max_matr)))
coordin_max_val.append(list_index_max_values_matr[max_matr.index(max(max_matr))])
print coordin_max_val