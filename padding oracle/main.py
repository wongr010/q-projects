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
            #print("We got: %d" % e.code)       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

def stringify_blocks(blocks):
    ans=''
    for index in range(len(blocks)):
        ans=ans+''.join(format(x, '02x') for x in blocks[index])

    return ans
                

if __name__ == "__main__":
    po = PaddingOracle()
    cipher="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
    CT_bytes=bytearray.fromhex(cipher)

    iv=CT_bytes[:16]
    starting_CT=CT_bytes[16:]

    b=[starting_CT[0:16], starting_CT[16:32], starting_CT[32:48]]
    iv_string=''.join(format(x, '02x') for x in iv)
    m=[]

    for index in range(len(b)):
        m.append([])

        guess=[0]*16
        for j in range(1, 17):
            pad=j
            print(j)
            pad = [0] * (16-j) + [pad]*j
            exited=False

            for i in range(128):

                if index>0:
                    c_prime=b[index-1].copy()

                else:
                    c_prime=iv.copy()

                guess[16-j]=i
                

                for k in range(0, 16):
                    
                    c_prime[k]= int(c_prime[k]) ^ guess[k] ^ pad[k]

                b1_string=''.join(format(x, '02x') for x in c_prime)
                end_string=''.join(format(x, '02x') for x in b[index])

                if index>0:
                    query_string=iv_string+stringify_blocks(b[:index-1])+b1_string+end_string
                
                if index == 0:
                     query_string=b1_string+end_string

                test=po.query(query_string)
                
                if test:
                   exited=True
                   m[index].insert(0, chr(i))
                   print(m[index])
                   break

            if not exited: #means that this is the start of the real padding
                guess[16-j]= j

            

    print(m)


