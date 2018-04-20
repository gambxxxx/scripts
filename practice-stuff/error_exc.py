def exception_handling():
    try:
        for i in ['a','b','c']:
            print (i**2)
        print('code weas executed correctly')
    except:
        print('Nuh Uh!')
    finally:
        print("c'monbruh!")

def main():
    exception_handling()

if __name__ == "__main__":
    main()
    
