def menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
# this menu function prints the same menu every time, saving space
def hex_char_decode(digit):
    deci = 0
    hex_digits = "0123456789ABCDEF"
    digit = digit.upper()
    for i in range(len(hex_digits)):
        if hex_digits[i] == digit:
            deci = i
            break
    return deci
# this function takes a hex character and turns it into a decimal
def hex_string_decode(hex):
    deci = 0
    hex_digits = "0123456789ABCDEF"
    power = 0
    if hex[1] == "x":
        hexy = hex[2:]
        hexy = hexy.upper()
        for digit in reversed(hexy):
            deci += hex_digits.index(digit.upper()) * (16 ** power)
            power += 1
    else:
        hexy = hex
        hexy = hexy.upper()
        for digit in reversed(hexy):
            deci += hex_digits.index(digit.upper()) * (16 ** power)
            power += 1
    return deci
def binary_string_decode(hex):
    deci = 0
    power = 0
    for i in reversed(hex):
        if i == '1':
            deci += 2 ** power
        power += 1
    return deci
# this function takes a binary character and turns it into a decimal
def binary_to_hex(binary):
    binary_to_hex_map = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }
    padding = 4 - (len(binary) % 4)
    if padding != 4:
        binary_str = '0' * padding + binary
    hexa = ''
    for i in range(0, len(binary), 4):
        n = binary[i:i+4]
        hexa += binary_to_hex_map[n]
    return hexa
# function takes a binary and turns it into a hex
def main():
    cond = True
    while cond:
        menu()
        op = int(input("Please enter an option: "))
        if op == 1:
            hex = input("Please enter the numeric string to convert: ")
            res = hex_string_decode(hex)
            print("Result:", res)
        elif op == 2:
            hex = input("Please enter the numeric string to convert: ")
            res = binary_string_decode(hex)
            print("Result:", res)
        elif op == 3:
            binary = input("Please enter the numeric string to convert: ")
            res = binary_to_hex(binary)
            print("Result:", res)
        elif op == 4:
            print("Goodbye!")
            cond = False
# cond = false immediatly stops the while loop and finishes the code

if __name__ == '__main__':
    main()

# line calls the main function

