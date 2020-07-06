name = "will"

decimalName = []
hexName = []
binName = []

for char in name:
  dexChar = ord(char)
  hexChar = hex(ord(char))
  binChar = bin(ord(char))
  decimalName.append(ord(char))
  hexName.append(hexChar)
  binName.append(binChar)

print("Hello world its me, " + name)
print("Hello world its me in ASCII decimal " + str(decimalName))
print("Hello world its me in ASCII hexadecimal " 
+ str(hexName))
print("Hello world its me in ASCII binary " + str(binName))

