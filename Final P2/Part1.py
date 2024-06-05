
def binary(n):
    p=n%2
    if n==1:
        return print('1',end='')
        
    elif n==0:
        return print('0',end='')
        
    elif p==1:
        n=n-1
        n=n//2
        print('1',end='')
        binary(n)
    else:
        n=n//2

        print('0',end="")
        binary(n)
binary(20)
