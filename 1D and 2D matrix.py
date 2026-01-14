# Write a Python program that reads 12 integer values from user, store values in Matrix of 4 X 3.
# Create another Matrix of 4 X 3, divide each element of Matrix1 by five, and store the result in the Matrix2.

rows = int(input('Enter the number of rows: '))
cols = int(input('Enter the number of columns: '))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input('Enter data in {} {} : '.format(i, j))))
    matrix.append(row)

print(matrix)
matrix2 = [[element // 5 for element in row]for row in matrix]
print(matrix2)
