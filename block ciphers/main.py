from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

def decrypt_cbc(ct_full, key):
	key=unhexlify(key)
	iv=unhexlify(ct_full[0:32])
	ct=ct_full[32:len(ct_full)]
	pt=[]
	previous_ct=iv
	cipher=AES.new(key, AES.MODE_ECB)

	for i in range(0, int(len(ct)/32)):
		start_index=i*32
		block=unhexlify(ct[start_index:start_index+32])
		decrypted=cipher.decrypt(block)
		print(decrypted)

		for j in range(0, len(decrypted)):
			pt.append(chr(decrypted[j] ^ previous_ct[j]))

		
		previous_ct=block
		

	print("".join(pt))
	return "".join(pt)


