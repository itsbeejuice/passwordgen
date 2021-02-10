import random

#shuffles string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 
lowercaseletter1=chr(random.randint(97,122))
lowercaseletter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
punct1=chr(random.randint(33,152))
punct2=chr(random.randint(33,152))
#Generate password using all the characters, in random order
password=uppercaseLetter1+uppercaseLetter2+lowercaseletter1+lowercaseletter2+digit1+digit2+punct1+punct2
password=shuffle(password)

print(password)