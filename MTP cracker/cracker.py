import binascii

def converttohex(mystring):
	hex_string=binascii.hexlify(mystring.encode())
	cipher=[]

	for i in range(0, len(mystring)):
	   
	    bytes_object = int(hex(ord(mystring[i])), 16)
	    cipher.append(bytes_object)

	return cipher

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
  decoded_strings.append(['*']*len(x))

todecode = strings[len(strings)-1]
decoded = ['*']*len(todecode)
space = 0x20
for cipher in strings:

	for i in range(0, len(cipher)):
		char=cipher[i]
		if i < len(todecode):
			attempt=char ^ todecode[i] ^ space
			if attempt > 0x60 and attempt < 0x7b or attempt > 0x40 and attempt < 0x5b or attempt == 0: #char or todecode[i] is a space
				decoded[i]= {i: chr(attempt)}

print(decoded)
guess=input("Guess input: ")
index=input("Input index: ")
str_i=int(input("Guess string: "))

#start guessing the plain texts. If its incorrect, the decoded text will turn into gibberish
while guess != "!":
	
	hex_guess=converttohex(guess)
	len_guess=len(hex_guess)
	ctr=0

	for (cipher, ds) in zip(strings, decoded_strings):
		beany=[]
		for i in range(int(index), min(len(cipher), int(index) + len(hex_guess))):
			
			char=chr(hex_guess[i-int(index)] ^ cipher[i] ^ strings[str_i][i])

			ds[i] = char
		print(str(ctr)+" "+"".join(ds))
		ctr=ctr+1

	guess=input("Guess input: ")
	index=input("Input index: ")
	str_i=int(input("Guess string: "))

