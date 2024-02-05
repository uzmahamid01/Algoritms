

# general way of doing fibonacci

def Fibonacci(n):
    if n<2:
        return n 
    return Fibonacci(n-1)+Fibonacci(n-2)


#Using DP
def FibonacciDP(n):
    seen = {}
    def recursefib(n):
        if n  in seen: 
            return seen[n]
        else:
            if n<2:
                return n 
            else:
                result=recursefib(n-1) + recursefib(n-2)
                seen[n]=result
                return result
    return recursefib


n = 9
print("Fibonacci({}) using regular recursion:".format(n), Fibonacci(n))

# Call the inner function to get the result for FibonacciDP
result_DP = FibonacciDP(n)(n)
print("Fibonacci({}) using dynamic programming:".format(n), result_DP)



