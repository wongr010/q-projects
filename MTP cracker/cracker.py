
def converttohex(mystring):
	return ''.join(r'\x{02:x}'.format(ord(c)) for c in mystring)

f = open("ciphers.txt", "r")
strings=[]
decoded_strings=[]
counter=1

for x in f:
  counter=counter+1

  if counter%2 == 1:
  	continue

  cipher=[]
  for i in range(0, len(x)-1, 2):
    bt=x[i]+x[i+1]
    bytes_object = int(bt, 16)
    cipher.append(bytes_object)

  strings.append(cipher)
  decoded_strings=['*']*len(x)

todecode = strings[len(strings)-1]
decoded = ['*']*len(todecode)
space = 0x20
for cipher in strings:

	for i in range(0, len(cipher)):
		char=cipher[i]
		if i < len(todecode):
			attempt=char ^ todecode[i] ^ space
			if attempt > 0x60 and attempt < 0x7b or attempt > 0x40 and attempt < 0x5b or attempt == 0: #char or todecode[i] is a space
				decoded[i]= chr(attempt)

print(decoded)
guess=""

while guess != "!":
	guess=input("Guess input: ")
	hex_guess=converttohex(guess)


