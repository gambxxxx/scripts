def zero_devision():
    x=5
    y=0

    try:
        z=x/y
        print('It was successfull')
    except:
        print("You can't do that")
    finally:
        print("All done!")

def main():
    zero_devision()

if  __name__ == "__main__":
    main()