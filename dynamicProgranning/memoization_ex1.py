# def addTo(n):
#     print("long time")
#     return n +80

#using global variable : not a  very good practice
cache =  {}
def memoizedAddTo1(n):
    
    if n in cache:
        return cache[n]
    else:
        print("long time")
        result = n+80
        cache[n] = result
        return cache[n]
    

def memoizedAddTo2(n):

    cache= {}  
    def memoize(n):
        if n in cache:
            return cache[n]
        else:
            print("long time")
            result = n+80
            cache[n] = result
            return cache[n]
    return memoize

memoize = memoizedAddTo2(5)
print (memoize(6))
print (memoize(7))


# print(addTo(10))  
# print(addTo(10))
print(memoizedAddTo1(10))
print(memoizedAddTo1(10))      
print(memoizedAddTo2(20)(20))
print(memoizedAddTo2(20)(20)) 