##
## Palindrome function
## Juliette Vintrou , id = 118 105 792
## Wednesday 10th October 2018
## CS 4801 - Introduction to Python , UCC
## Assignment 2
##


## Definition of the functions

def is_palindrome(s):
    """
    This function is_palindrome returns a boolean if the string which represents
    the word can be read the same from left to right and right to left.

    1. transform the string in lower_case string
    2. For every letter check if the -(k+1)th letter
       is the same as the (k)th letter 
    3. if the total of same letter in the word is equal to half the length
       of the word then it's a palindrome
    
    Input  : s (a word - string)
    Output : is_palin (boolean)

    Example: is_palin = is_palindrome("Abba")

    word :Abba
    The following word is a palindrome : True
    
    """
    total = 0
    new_s = s.lower()
    is_palin = False

    for i in range (0,len(new_s)//2) :
        if (new_s[i] == new_s[-(i+1)]):
            total = total + 1
            
    if total == len(new_s)//2 :
        is_palin = True
        
    return is_palin

## Start the program with a printing function        
print("cs 4801 , assigmnemt 2 : is palindrome function")

## Ask the user to enter parameters
print("Enter a word that you want to know if it's a palindrome ?")
s = (input("word :"))

## Call the function 
is_palin = is_palindrome(s)

print("The following word is a palindrome : "+ str(is_palin))


