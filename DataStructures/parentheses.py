from pythonds.basic import Stack

def parChecker(symbol_string):
        
        #algorithm
        s = Stack()
        l = 0
        isBalanced = True

        while l < len(symbol_string) and isBalanced:
            symbol = symbol_string[l]
            if symbol in "([{":
                s.push(symbol)

            else:
                if s.isEmpty():
                    isBalanced = False
                else:
                    top = s.pop()
                    if not matches(top, symbol):
                        isBalanced = False
            
            l += 1
        
        if isBalanced and s.isEmpty():
            return True
        else:
            return False
        
def matches(open, close):
    openers = "([{"
    closers = "}])"

    return openers.index(open) == closers.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
# def main():
#     symbol_string = input("Enter a string containing parentheses, square brackets, and curly braces: ")
#     if parChecker(symbol_string):
#         print("The parentheses, square brackets, and curly braces are balanced.")
#     else:
#         print("The parentheses, square brackets, and curly braces are not balanced.")

# if __name__ == "__main__":
#     main()