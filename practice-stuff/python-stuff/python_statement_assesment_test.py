st='Sam print only the words that start with s in this sentence'
st1='Print every word in this sentence that has an even number of letters' 
     for word in st.split():
            if word[0].lower() == 's':
            print(word)

    for num in range (0,11,2): #Range
        print(num)

print([x for x in range (1,51) if x%3==0])

for word in st1.split():
    if len(word)%2==0:
        print(word + 'is even')

for num in range(1,101):
    if(num%3==0 and num%5==0):
        print('FizzBuzz')
    elif (num%3===0):
        print('Fizz')
    elif(num%5==0):
        print('Buzz')
    else:
        print(num)

st2='create a list for first letters in this sentence'
print([x[0] for x in st2.split() ])