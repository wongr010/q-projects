from decimal import Decimal
import math
import threading


hash_table={}

def modInverse(b,m): 
    g = math.gcd(b, m)  
    if (g != 1): 
        return -1
    else:  
        return pow(b, m - 2, m) 

def modDivide(a,b,m): 
    a = a % m 
    inv = modInverse(b,m) 
    if(inv == -1): 
        return None
    else: 
        return ((inv*a) % m) 

def update_ht(i):
	print("modDivide ", i)
	moo=modDivide(h, pow(g, i), p)
	if moo is not None:
		hash_table[moo]=i


g=11717829880366207009516117596335367088558084999998952205
h=323947510405045044356526437872806578864909752095244
p=134078079299425970995740249982058461274793658205923933
B=math.pow(2, 20)
x1=0
x0=0

for i in range(int(B)):
  x = threading.Thread(target=update_ht, args=(i,))
  x.start()
  x.join()	



 

