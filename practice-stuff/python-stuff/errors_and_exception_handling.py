try:
    f=open('testfile','r')
    f.write("write test file")
except TypeError:
    print("there was a  TypeError!")
except:
    print("All other exceptions")
finally:
    print("I always run")