from pythonds.basic import Stack
def divideby2(num):
    remstack = Stack()
    while num > 0:
        rem = num % 2
        remstack.push(rem)
        num = num // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

def main():
    num = int(input("Enter a decimal number: "))
    binary = divideby2(num)
    print(f"The binary representation of {num} is: {binary}")

if __name__ == "__main__":
    main()