"""
Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2 c,2 b,2 e,1 d,1 g,1 f,1
Use str.join() method and dict comprehension for print result
"""

letters = input("Введіть букви ")

counted_letters = {}
for letter in letters:
    counted_letters[letter] = counted_letters.get(letter, 0) + 1

    #counted_letters = ''.join(key + counted_letters(val) for key, val in counted_letters.items())
    print(counted_letters)

