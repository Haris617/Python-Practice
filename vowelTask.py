# Task 01:
# Write a C++ program that counts the number of vowels and their frequencies in a given string.
# The program should ask the user to enter a sentence or a string of their choice.
# It should then analyze the string and calculate the total count of vowels present, as well as the frequency of each vowel
# (i.e., the number of times each vowel appears in the string).
# The program should consider both uppercase and lowercase letters as vowels.
# In addition to counting the vowels and their frequencies, your program should include the following:
# •	Proper user prompts and informative messages to guide the user throughout the program.
# •	Input validation to handle cases where the user enters an empty string or a string without any vowels.
# •	Display the total count of vowels in the string, followed by the frequency of each vowel (both uppercase and lowercase) in a tabular format.
# •	Utilize an array to store the count of each vowel. The array should have a size of 10, corresponding to the 5 vowels (A, E, I, O, U) in both uppercase and lowercase.

sentence = str(input('Enter a Sentence : '))

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowelCount = [0] * 10


for char in sentence:
    if char in vowels:
        Index = vowels.index(char)
        vowelCount[Index] += 1

total_vowels = sum(vowelCount)

if total_vowels == 0:
    print('No vowels found')

else:
    for v, c in zip(vowels, vowelCount):
        print('{} : {}'.format(v, c))

