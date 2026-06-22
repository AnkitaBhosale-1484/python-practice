b=bytes([65,66,67])
print(b)

"""output
b'ABC'
bytes() expects values in the range 0 to 255.
Each number is treated as an ASCII/byte value.
Python converts each number to its corresponding character.
Number	ASCII Character
65 A 66 B 67 C

"""