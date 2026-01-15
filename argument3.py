def factorial(x):
    '''this is a recursive function to find factorial of a integer'''
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
print(factorial.__doc__)
print("the factorial for 0 is :",factorial(0))
print("the factorial for 1 is :",factorial(1))
print("the factorial for 2 is :",factorial(2))
print("the factorial for 5 is :",factorial(5))
print("the factorial for 10 is :",factorial(10))
