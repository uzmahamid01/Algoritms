def str_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        print(s2+s2)
        return s1 in s2 + s2
    return False
        
def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    print(str_rotation(s1, s2))

main()
