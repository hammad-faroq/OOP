def fib(n):
    """This is simplple fibonacci mehod but a bit lenghty with one extra elif statement"""
    for i in range(n):
        if i==0:
            previous1=i
            previuos2=i
            f=previous1+previuos2
        elif i==1:
            previous1=f
            previuos2=i
            f=previuos2+previous1
        elif i==2:
            previous1=0
            previuos2=1
            f=previous1+previuos2
            previous1=f
        else:
            previous2 = previous1
            previous1 = f
            f=previous2+previous1

        if i==n-1:
            print(f,end="")
        else:
            print(f,end=',')

# fib(20)

def fib1(n):
    """This is the fibonacci function which will give you all the numbers as per input"""
    for i in range(n):
        if i==0:
            previous1=i
            previuos2=i
            f=previous1+previuos2
        elif i==1:
            previous1=f
            previuos2=i
            f=previuos2+previous1
        else:
            previous2 = previous1
            previous1 = f
            f=previous2+previous1
        if i==n-1:
            print(f,end="")
        else:
            print(f,end=',')
fib1(20)