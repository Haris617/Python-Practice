#Write a program that first stores 10 integers in an array and displays an element present in an array.
#The program should then multiply each element with 3 and display the resultant array.

listA = []

print('Enter Size of List : ')
size = int(input())

print('Enter Data : ')
for i in range(size):
    listA.append(int(input()))


for i in range(size):
    listA[i] *= 3

print(listA)


# Write a program to search Value for Specific Index in an array.
# it should prompt the user to enter Index to search for Element in the array.

print('Enter Index to Search in List')
index = int(input())

try:
    print('Data is ',  listA[index])
except Exception as error:
    print(f"Error Error : {error}")

# The program should find the key value and display its index if it exists in the array.
# If the key value is not found, it should display a message indicating that the element was not found in the array.

print('Enter Key Value')
key = int(input())

if key in listA:
    print('Index : ', listA.index(key))

else:
    print('Not Found')

# Write a program to find the even numbers in an array of 10 integers.
# The program should first take input from the user and display an element present in an array.
# Then the program should find and display those elements only that are even.
# Also calculate the total number of even numbers in an array.

listB = []
evenNumber = 0

for i in range(10):
    print('Enter Data : ', end = '')
    listB.append(int(input()))

print('List is : ', listB)

print('List with even Number is : ')
for i in range(10):
    if listB[i] % 2 == 0:
        evenNumber += 1
        print(listB[i])

print('Even Number Count : {}'.format(evenNumber))

