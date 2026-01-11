def print_formatted(number):
    width = len(bin(number)) - 2  # width of binary representation

    for i in range(1, number + 1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(dec.rjust(width),
              octal.rjust(width),
              hexa.rjust(width),
              binary.rjust(width))
