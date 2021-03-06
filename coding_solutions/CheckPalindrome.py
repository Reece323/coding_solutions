"""

A palindrome is a word, phrase, number, or another sequence of characters 

that reads the same backward or forward. This includes capital letters, 

punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid 

palindrome.

"""

def csCheckPalindrome(input_str):
    return input_str == input_str[::-1]