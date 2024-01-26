def recur(n):##This uses the stack memory for storing the methods if there are still statements to execute after the recursion and this uses last in first out strategy.
    if n <1:
        print("n is less than 1")
    else:
        recur(n-1)
        print(n)
# recur(4)

def factorial(n):
    assert n>=0 and int(n)==n,"the number needs to be positive :)"#This is the assert keyword to check the case of the wrong entry eg int less than 0 or a float :)
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
# print(factorial(-4))
def fibonacci(n):##This functoin will give the fibonacci number of the sequence at the given input position
    assert n>=0 and int(n)==n,"o ho!"
    if n in [0,1]:
        return n
    else:
        return factorial(n-1) + factorial(n-2)##I think I just to understand how the recursion works and just put the formula base case and error in the fucntion
# print(fibonacci(6))
def sum_of_digits(n):
    assert n>=0 and int(n)==n,"Number needs to be positive integer!"
    if n==0:
        return 0
    return int(n%10)+sum_of_digits(int(n/10))
# print(sum_of_digits(12))

def power_of_a_numeber(base,exponent):
    assert exponent>=0 and int(base)==base,"Base needs to be positive and exponent needds to be positive"
    if exponent==1:
        return base
    if exponent==0:
        return 0
    return base*power_of_a_numeber(base,exponent-1)
# print(power_of_a_numeber(8,3))
def to_binary(n):
    """This method will generate any number in binary.We just nedd the recursive case and the stop condition.Exception is just optional"""
    assert int(n)==n,"Number must be positive integer only!"
    if n==0:
        return 0
    return n%2+10*to_binary(n//2)
print(to_binary(13))