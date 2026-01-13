List = ['a','b','c','d']

#copyList
List2 = List[:]

#adding Element in List
List.append('e')

#Length of List
print(len(List))

#Mutiple Elemental List
List3 = ['X', 'Y', 'Z'] * 3

#Adding List
List4 = ['A','B','C']
List5 = ['D','E','F']
List6 = List4 + List5

#deleting List
del List6[0]

#List in for Loop
Names = ['haris', 'wasim', 'yasir', 'usman']
for i, name in enumerate(Names):
    print(f"Index is {i}, Name is {name}")

#2 Lists in For Loop
ListName = ['Haris', 'Wasim', 'Shafey']
ListAge  = [18,19,20]

for n, a in zip(ListName, ListAge):
    print(f"{n} is {a} years old")

#Check if Element is Available in List or not
ListAlphabet = ['a','b','c','d']
print('z' in ListAlphabet)

#Assigning Element of List to Variables
ListCat = ['Orange', '18', 'Fat']
color, age, size = ListCat
print(color, age, size)

#Swap Trick
a = 'apple'
b = 'ball'
a,b = b,a
print(a,b)

#Adding String
word = 'Hello '
word+= 'world'
print(word)

#removing Specific Element from List
listAlphabet = ['a','b','c','d']
listAlphabet.remove('b')
print(listAlphabet)

#sorting ascending Order
ListNumber = [5,4,3,2,0,8,4]
ListNumber.sort()
print(ListNumber)

#sorting Descending Order
ListNumber.reverse()
print(ListNumber)
ListNumber.sort(reverse=True)
print(ListNumber)








