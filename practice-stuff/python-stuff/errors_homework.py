try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("No integers found")
finally:
    print("Make sure to provide integers in order to get squares!...")

print('\n\n')
x=5
y=0
try:
    z= x/y
except:
    if x==0 or y==0:
        print("Whoops! Can't divide with zero! ")
finally:
    print("We can't divide with zero! ")

while True:
    value=int(input('Please input an integer'))
    try:
        if type(value) is int:
            print("Thank you!, number squared is {} ".format(value**2))
            break
    except:
            print("An error occurred, please try again...")
            
    finally:
        decision=input("would you like to try again? type y for Yes and n for No ")
        if(decision=='n'):
            break
        else:
            pass
        