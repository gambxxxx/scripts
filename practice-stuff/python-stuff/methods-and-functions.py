mylist=[1,2,3]
help(mylist.insert)

def name_of_function(name):
    

def add_function(num1,num2):
    return num1+num2

def pig_latin(word):
    first_letter=word[0]
    #chek if vowel

    if first_letter in 'aeiou':
        pig_word=word+'ay'
    else:
        pig_word=word[1:]+first_letter+'ay'

    return pig_word
print(pig_latin('word'))