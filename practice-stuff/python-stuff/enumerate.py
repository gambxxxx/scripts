index_count = 0
word='abcde'
for letter in word:
    print(word[index_count])
    index_count+=1


for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')