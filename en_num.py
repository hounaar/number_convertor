

def letters_to_num(letters):
        numbers = []
        for letter in letters:
            number = ord(letter) - 96
            numbers.append(number)

            print(numbers)




print(letters_to_num(input("letter to numbers :\n")))

print(chr(65))