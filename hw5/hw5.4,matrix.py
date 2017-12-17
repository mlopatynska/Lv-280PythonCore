import random

def maxelem (matrix1,matrix2):
    large1=0
    for i in matrix1:
        if max(i)>large1:
            large1=max(i)
            ind1=i.index(large1)
            if large1 in i:
                index1=matrix1.index(i)
                #print index
        else:
            large1=large1
    print ('The biggest number in matrix1 is {} '.format(large1))
    print ('Its index in matrix1 is [{}][{}]'.format(index1,ind1))
    large2 = 0
    for i in matrix2:
        if max(i) > large2:
            large2 = max(i)
            ind2 = i.index(large2)
            if large2 in i:
                index2 = matrix2.index(i)
                # print index
        else:
            large2 = large2
    print ('The biggest number in matrix2 is {} '.format(large2))
    print ('Its index in matrix2 is [{}][{}]'.format(index2, ind2))
    #print matrix1
    matrix1[index1].remove(matrix1[index1][ind1])
    #print matrix1
    matrix1[index1].insert(ind1,large2)
    print matrix1
    matrix2[index2].remove(matrix2[index2][ind2])
    # print matrix2
    matrix2[index2].insert(ind2, large1)
    print matrix2








matrix1 = [[random.randint(1, 100) for x in range(5)] for y in range(5)]
matrix2 = [[random.randint(1, 100) for x in range(5)] for y in range(5)]
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        print matrix1[i][j],
    print
print ('')
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        print matrix2[i][j],
    print


maxelem (matrix1,matrix2)

