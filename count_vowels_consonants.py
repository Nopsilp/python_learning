"""
Learning Objective: 
    Practice working with control flow constructs and string manipulation.

Exercise: 
    Write a Python program that takes a string as input and performs the following tasks:
        Count the number of vowels (a, e, i, o, u) in the string.
        Count the number of consonants (all alphabetic characters excluding the vowels) in the string.
        Print the counts of vowels and consonants.

Requirements:
    Define a function count_vowels_consonants that takes a string as input and returns the counts of vowels and consonants as a tuple.
    Inside the function, use a for loop to iterate over each character in the string.
    Use conditional statements to determine if a character is a vowel or a consonant, and increment the respective count accordingly.
    After counting the vowels and consonants, return the counts as a tuple (vowel_count, consonant_count).
    Prompt the user to enter a string.
    Call the count_vowels_consonants function with the user input as an argument.
    Print the counts of vowels and consonants in the format "Number of vowels: X" and "Number of consonants: Y", where X and Y are the respective counts.
"""

def count_vowels_consonants(string):
    vowel = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char.lower() in vowel:
            vowel_count += 1
        else:
            consonant_count +=1
    return vowel_count, consonant_count

user_string = input("Enter a string here:")

result = count_vowels_consonants(user_string)
print("Number of vowels: {0} and Number of consonants: {1}".format(result[0], result[1]))

