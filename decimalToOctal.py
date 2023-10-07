"""
File: decimalToOctal.py
Converts a decimal integer to a octal integer.
"""

decimal=int(input('Enter a decimal integer: '))
print("\nQuotient Remainder Octal")
i = 1
octalNum = 0
num=""
while (decimal != 0):
    rm = decimal % 8
    decimal //= 8
    octalNum = octalNum + rm * i
    i *= 10
    num = str(rm)+num
    print("%5d%8d%12s" % (decimal, rm, num))
print('The octal representation is ',octalNum)
