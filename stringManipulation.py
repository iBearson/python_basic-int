import re

def reverse_words(sentence):
    words = re.findall(r'\w+|[^\w\s]|\s', sentence)
    
    #reverse only alphanumeric words
    reversed_words = [word[::-1] if word.isalnum() else word for word in words]
    
    #retrieve reversed texts
    result = ''.join(reversed_words)
    
    return result

sentence = input("Enter a sentence to reverse the words: ")
print(reverse_words(sentence))

