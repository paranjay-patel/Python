#unlimited positional arguments in function 

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,4,5,6,7,8,9,3)

#unlimited keyword arguments in function 

def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=2,multiply=3)