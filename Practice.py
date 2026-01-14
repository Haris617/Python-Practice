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

#Convert Tuple to List
TupleA = ('a','b','c','d')
ListA = list(TupleA)
ListA[0] = 'e'
print(ListA)

#Found Element in Tuple
if 'b' in TupleA:
    print('Found')

#Dictionary
Dict1 = {'Name' : 'Haris', 'Age' : 19, 'CGpa' : 3.59}
print(Dict1)

#Printing Dict Keys
for i in Dict1.keys():
    print(i)

#Printing Dict Values
for i in Dict1.values():
    print(i)

#Printing Items
for i in Dict1.items():
    print(i)

for k, v in Dict1.items():
    print('Key {}, Value {}'.format(k, v))

#Checking if Key or Value Exist
print('Name' in Dict1.keys())
print('Wasim' in Dict1.values())

#Checking ifNoKey return 0 else value of Key
Dict2 = {'Apple' : 10, 'Mango' : 5}
print('I have {} apples'.format(Dict2.get('Apple', 0)))
print('I have {} eggs'.format(Dict2.get('eggs')))

#Adding if key is Not in Dictionary
Dict2.setdefault('Banana', 12)
print(Dict2)

#Merging Dictionary
Dict_a = {'a' : 10, 'b' : 20, 'c' : 30}
Dict_b = {'b' : 30, 'c' : 40}
Dict_c = {**Dict_a, **Dict_b}
print(Dict_c)

#sets is Used for No Duplicate Entries
#Support Union, Intersection etc

#adding element in Set
set1 = {1}
set1.add(2)
set1.add(5)

print(set1)

#adding Multiple Elements in Set
set1.update({2,3,4,5,6})
print(set1)

#Removing Element From Set
print('Enter Element to Remove')
element = int(input())

try:
    set1.remove(element)
except Exception as error:
    print('Error: {}'.format(error))
finally:
    print('Set is : ', set1)

#Removing Element From Set (if Element is not in Set, it Will not Show Error
print('Enter Element to Discard / Remove')
element = int(input())
set1.discard(element)
print(set1)

#Union and Intersection
set1 = {1,2,3}
set2 = {3,4,5}
set3 = {3,6,7}
print(set1.union(set2))
print(set1.intersection(set2, set3))









