
def create_matrix(n,m):
    import random
    matrix = [[random.randint(1, 100) for x in range(n)] for y in range(n)]
    return matrix

def create_mas(n):
    import random
    matrix = [random.randint(1, 100) for x in range(n)]
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print matrix[i][j],
        print

def mx(matrix):
    maxim=matrix[1][1]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if maxim<matrix[i][j]:
                maxim=matrix[i][j]
                n=i
                m=j
    return [n,m]

def my_sort(matrix):
    n=1
    while n<len(matrix):
        for i in range(len(matrix)-n):
            if matrix[i]<matrix[i+1]:
                matrix[i],matrix[i+1] = matrix[i+1],matrix[i]
        n+=1
    return matrix

A=create_matrix(5,5)
B=create_matrix(5,5)

print_matrix(A)

print 'Maximum A[{},{}]={}'.format(mx(A)[0]+1,mx(A)[1]+1,A[mx(A)[0]][mx(A)[1]])

print_matrix(B)
print 'Maximum B[{},{}]={}'.format(mx(B)[0]+1,mx(B)[1]+1,B[mx(B)[0]][mx(B)[1]])

A[mx(A)[0]][mx(A)[1]],B[mx(B)[0]][mx(B)[1]]=B[mx(B)[0]][mx(B)[1]],A[mx(A)[0]][mx(A)[1]]
print_matrix(A)
print '---------------------'
print_matrix(B)
print '-----Sort -----'
x=create_mas(5)
print x
print my_sort(x)

y=create_mas(10)
print y
print my_sort(y)


