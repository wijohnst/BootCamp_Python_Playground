#Will Johnston's version of the Caesar Cypher

#List with each letter of the alphabet
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Function that encrypts a message
def encryptMessage(userMessage,steps):
  print('Encrypting message...')

  encryptedMessage = []

  userMessage = userMessage.replace(" ", "")
  #Loops through the message and encrypted letter
  for x in userMessage.upper():
    steppedIndex = alphabet.index(x) + int(steps) 
    if steppedIndex % 26 < 1:
      encryptedMessage.append((alphabet[steppedIndex % 26]))
    else:
      encryptedMessage.append((alphabet[steppedIndex]))

  
  print("".join(encryptedMessage))


#Prompt for user input
print('Hello Comrad! What is your message?')

#This wil be the message that we want to encrypt
userMessage = input()

print('Your unencrypted message =' + ' ' + '\"' + userMessage + '\"')

print('Continue (Y/N)?')

continue_1 = input()

#These values are used to compare the user's response to continue or not
affirmativeResponse = "Y"
negativeResponse = "N"

#Compares user Answer
if continue_1 == affirmativeResponse:
  print('How many steps in your cypher?')
  #This value will determine how many steps to add to the cypher
  steps = input()
  encryptMessage(userMessage,steps)
  
else:
  print('Goobye')
  exit()