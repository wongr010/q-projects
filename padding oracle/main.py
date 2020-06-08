import urllib3
import urllib
import urllib.parse
import urllib.error
import urllib.request
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib.parse.quote(q)    # Create query URL
        #req = urllib.request.urlopen(target)         # Send HTTP request to server
        try:
            f = urllib.request.urlopen(target)          # Wait for response
        except urllib.error.HTTPError as e:          
            print("We got: %d" % e.code)       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

if __name__ == "__main__":
    po = PaddingOracle()
    cipher="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
    CT_bytes=bytearray.fromhex(cipher)

    iv=CT_bytes[:16]
    starting_CT=CT_bytes[16:]

    b=[starting_CT[0:16], starting_CT[16:32], starting_CT[32:48]]
    iv_string=''.join(format(x, '02x') for x in iv)
    m=[]

    for index in range(1):
        guess=[0]*16
        for j in range(1, 17):

            pad = [0] * (16-j) + [j]*j

            for i in range(256):

                c_prime=b[index].copy()

                if index==0:
                    c_prime=iv.copy()
                guess[16-j]=i

                if i==0:
                    print(pad)
                    print(guess)
                    
                for k in range(0, 16):
                    
                    c_prime[k]= int(c_prime[k]) ^ guess[k] ^ pad[k]

                b1_string=''.join(format(x, '02x') for x in c_prime)
                
                query_string=iv_string+b1_string+''.join(format(x, '02x') for x in b[index])
                
                if index == 0:
                     query_string=b1_string+''.join(format(x, '02x') for x in b[index])

                test=po.query(query_string)
                if i == 0:
                    print(query_string)
                if test:
                   print(query_string)
                   m.insert(0, chr(i))
                   print(m)
                   break
    print(m)
#     #po.query(sys.argv[1])       # Issue HTTP query with the given argument

# import sys
# import urllib
# import sys


# ct = bytearray.fromhex('f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4')
# charset=''.join([chr(i) for i in range(0,256)])

# TARGET = 'http://crypto-class.appspot.com/po?er='

# def strxor(s1,s2):    
#     # convert strings to a list of character pair tuples
#     # go through each tuple, converting them to ASCII code (ord)
#     # perform exclusive or on the ASCII code
#     # then convert the result back to ASCII (chr)
#     # merge the resulting array of characters as a string
#     return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

# # Chaing one byte t string [Manually]
# def str_set_chr(s, idx, value):
#     s = list(s)
#     s[idx] = value
#     return ''.join(s)

# # def padding_oracle_request(ct):
# #     url = TARGET + ct.encode('hex')
# #     req = urllib2.Request(url)
# #     try:
# #         f = urllib2.urlopen(url)
# #     except urllib2.HTTPError, e:
# #         if e.code != 404:
# #             return False
# #     return True

# def padding_oracle_request(ct):
#     target = TARGET + ct.encode('hex')    # Create query URL
#     #req = urllib.request.urlopen(target)         # Send HTTP request to server
#     try:
#         f = urllib.request.urlopen(target)          # Wait for response
#     except urllib.error.HTTPError as e:          
#         print("We got: %d" % e.code)       # Print response code
#         if e.code == 404:
#             return True # good padding
#         return False # bad padding

# def block_join(arr):
#     joined=[]
#     for block in arr:
#         joined=joined+block

#     return joined


# def padding_oracle(ct, charset):
#     guess_pt = ''
#     iv = ct[:16]
#     ct = ct[16:]
#     ct_blocks = [ct[0:16], ct[16:32], ct[32:48]]

#     for i in range(-1, len(ct_blocks)-1):
#             if i >= 0:
#                 target = ct_blocks[i]
#             else:
#                 target = iv
#             guess_block = "\x00"*16
#             for j in range(1,len(target)+1):
#                 padding = "\x00"*(16-j)+chr(j)*j
#                 for ch in charset:
#                     if ch == '\x01' and i == len(ct_blocks)-2:
#                         continue
#                     guess_block = str_set_chr(guess_block, 16-j, ch)
#                     print(strxor(guess_block, padding))
#                     new_target = strxor(target.decode("utf-8"), strxor(guess_block, padding))
#                     if i >= 0:
#                         ct_blocks[i] = new_target
#                     else:
#                         iv = new_target
#                     sys.stdout.write("TRY %s [%s] => [%s]\r" % ((iv + block_join(ct_blocks[:i+2])).encode('hex'), guess_block.encode('hex'), guess_pt.encode('hex')))
#                     sys.stdout.flush()
#                     if padding_oracle_request(iv + block_join(ct_blocks[:i+2])) == True:
#                         break
#             guess_pt += guess_block
#     return guess_pt 

# def main(argv):
#     pt = padding_oracle(ct, charset)
#     print("Decrypted::", pt)

# if __name__ == "__main__":
#         main(sys.argv)