def ispower10(n):
    if  n <= 0: 
        return False
    
    while n > 1:
        if n % 10 != 0:
            return False
        n/= 10
    return True

print(ispower10(100)) 
