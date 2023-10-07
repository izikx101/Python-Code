"""
File: octalToDecimal.py
Converts a octal integer to a decimal integer.
"""

octalNum=int(input('Enter a string of octal digits: '))
i = 1
decimal = 0
while (octalNum != 0):
    rmd = octalNum % 10
    octalNum //= 10
    decimal += rmd * i
    i *= 8
print('\nThe integer value is ',decimal)
