def square(num):
    return num**2
my_list=[1,2,3,4,5]
for item in map(square,my_list):
    print(item)

print(list(map(square,my_list)))