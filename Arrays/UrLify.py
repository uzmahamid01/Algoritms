def urlify(input, n):
    new_input = list(input)
    result = []
    for i in range(n):
        if new_input[i] == ' ':
            result.append('%20')
        else:
            result.append(new_input[i])
        
    
    return ''.join(result)


def main():
    input = "Mr John Smith  "
    n = 13
    print(urlify(input, n))


main()
