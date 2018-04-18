def ask_for_int():
    while True:
        try:
            result=int(input("Please provide number: "))
        except:
            print("Whoops! That's not a number")
            continue
        else:
            print("Yes, thank you! ")
            break
        finally:
            print("End of try/except/finally")

ask_for_int()