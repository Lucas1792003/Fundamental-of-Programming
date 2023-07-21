def SublistSearch(mat, key):
    for j in range(len(mat)):
        for i in range(len(mat[0])):
            if mat[j][i] == key:
                if (i+1) < len(mat[0]) and mat[j][i+1] == key:
                    return j + 1, i + 1
                elif (i-1) >= 0 and mat[j][i-1] == key:
                    return j + 1, i
    return -1, -1

mat = [
    [1, 2, 3, 4, 5, 6],
    [9, 10, 11, 12, 13, 14],
    [21, 22, 23, 24, 25, 26]
]

key = int(input("Enter a number you want to search: "))
row, column = SublistSearch(mat, key)

print('For matrix:')
for m in mat:
    print(m)
print('====================================')
if row != -1:
    print(f'The key, {key}, found at row# {row} and column# {column}.')
else:
    print(f'Sorry, {key} could not be found.')
