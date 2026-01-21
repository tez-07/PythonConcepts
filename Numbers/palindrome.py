
#if a string/Number is reversed its the same.

#Palindrome Check for String
def palindrome(sentence):

    reversed =  sentence[::-1]
    if reversed.lower() == sentence.lower():
        print(f'{sentence} is palindrome')
    else:
        print(f'{sentence} is not a palindrome')

palindrome('pup')


#Palindrome Check for Number
def palindromeNumber(num):

    original = num
    reverse = 0
    while num > 0:
        remainder = num % 10
        reverse = remainder  + reverse* 10
        num = num // 10

    if original == reverse:
        print(f'{original} is palindrome')
    else:
        print(f'{original} is not a palindrome')

palindromeNumber(1)
palindromeNumber(121)
palindromeNumber(123)