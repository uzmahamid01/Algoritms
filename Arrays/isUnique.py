# 1.1 Determine if a string has all unique characters, no additional data structures allowed 
# the time complexity of the below algorithm will be O(n^2) and space as well.
def isUnique(x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j]:
                return False
        
    return True
    
def main():
    x = "44"
    print(isUnique(x))
    x = "117"
    print(isUnique(x))
    x = "132"
    print(isUnique(x))

main()