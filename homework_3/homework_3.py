#palindrome
# Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'

def isPalindrome(word):
    return word == word[::-1]


word = input("Введіть, будьласка, слово ")
result = isPalindrome(word)

if result:
    print("+")
else:
    print("-")