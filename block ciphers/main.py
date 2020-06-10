from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify
from math import ceil

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

		for j in range(0, len(decrypted)):
			pt.append(chr(decrypted[j] ^ previous_ct[j]))
		
		previous_ct=block
		
	print("".join(pt))
	return "".join(pt)

def decrypt_ctr(ct_full, key):
	key=unhexlify(key)
	iv=unhexlify(ct_full[0:32])
	ct=ct_full[32:]
	cipher=AES.new(key, AES.MODE_ECB)
	pt=[]

	for i in range(ceil(len(ct)/32)):
		ct_int=int.from_bytes(iv, byteorder="big") 
		ct_bytes=(ct_int + i).to_bytes(16, 'big')
		nonce=cipher.encrypt(ct_bytes)
		start_index=i*32
		block=unhexlify(ct[start_index:min(start_index+32, len(ct))])

		for j in range(0, len(block)):
			pt.append(chr(nonce[j] ^ block[j]))

	print("".join(pt))
	return "".join(pt)





decrypt_cbc("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81", "140b41b22a29beb4061bda66b6747e14")
decrypt_cbc("5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253", "140b41b22a29beb4061bda66b6747e14")
decrypt_ctr("69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329", "36f18357be4dbd77f050515c73fcf9f2")
decrypt_ctr("770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451", "36f18357be4dbd77f050515c73fcf9f2")