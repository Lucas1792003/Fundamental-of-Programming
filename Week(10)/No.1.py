#6511171_Wai_Yan_Paing_class10_section542_Q1
def matrixMultiplication(a,b):
    result = [[0 for k in range(len(a[0]))] for k in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
size = int(input('For 1st matrix. How many column do you want?: ')) 
a = []
for x in range(size):
    a.append([int(y) for y in input('Enter each row separately: ').split()])
size = int(input('For 2nd matrix. How many column do you want?: ')) 
b = []
for i in range(size):
    b.append([int(j) for j in input('Enter each row separately: ').split()])
print('Matrix A: ',a)
print('Matrix B: ',b)
print('Matrix A x B: ',(matrixMultiplication(a,b)))