def ask():
   
    while True:
        number=input("please input an integer")
        try:
            print(int(number)**2)
            break
        except:
            print("Whoops! An error occurred! Please try again")
        else:
            print("Thank you for inputing an integer.")

def main():
    ask()

if __name__ == "__main__":
    main()