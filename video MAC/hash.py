from Crypto.Hash import SHA256
from functools import partial

chunks=[]

with open('6.1.intro.mp4_download', "rb") as f:
	for chunk in iter(partial(f.read, 1024), b''):
		chunks.append(chunk)

hashes=[]
lasthash=b''
for i in reversed(chunks):
	
	hash_object = SHA256.new(data=(i+lasthash))
	hashes.insert(0, hash_object.hexdigest())
	lasthash=bytearray.fromhex(hash_object.hexdigest())

print(hashes[0])

