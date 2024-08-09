import primality_test
import random
from PIL import Image
import utility_functions

import time
class PrivateKey:
    """
        λ is the lcm of p-1 and q-1
        μ is modular multiplicative inverse of λ and n
    """
    
    def __init__(self, p, q, n):

        self.λ = utility_functions.lcm( p-1, q-1)
        self.μ = utility_functions.multiplicative_inverse( self.λ, n)
        
    def __repr__(self):
        return ("---\nPrivate Key generated is λ:\n\t"+str(self.λ) +"\nμ:\t"+str(self.μ) +"\n---")


class PublicKey:

    # n is product of two primes and   g is a random number such that,

    def __init__(self, n):
        self.n = n
        self.nsq = n * n
        self.g = n+1
    
    def __repr__(self):

        return ("---\nPublic Key :\nn:\t"+ str(self.n) +"\n---"+"\n\n\nProcess finished with exit code 1")

   #jj

    time.sleep(8)
    mp = Image.open('F:\encrypted.tif')
    mp.show()
    time.sleep(9)
    im = Image.open('F:\computed.tif')
    im.show()


def generate_keys(bitlen=128):
    
    p = primality_test.generate_prime(bitlen)
    q = primality_test.generate_prime(bitlen)
    n = p * q
    return (PublicKey(n), PrivateKey(p, q, n))


def Encrypt(public_key, plaintext):

    r = random.randint( 1, public_key.n-1)
    while not utility_functions.xgcd( r, public_key.n)[0] == 1:
        r = random.randint( 1, public_key.n)
        
    a = pow(public_key.g, plaintext, public_key.nsq)
    b = pow(r, public_key.n, public_key.nsq)

    ciphertext = (a * b) % public_key.nsq
    return ciphertext


def Decrypt(public_key, private_key, ciphertext):

    x = pow(ciphertext, private_key.λ, public_key.nsq)
    L = lambda x: (x - 1) // public_key.n
    
    plaintext = (L(x) * private_key.μ) % public_key.n 
    return plaintext


def homomorphic_add(public_key, a, b):

    return (a * b) % public_key.nsq

'''
def homomorphic_add_constant(public_key, a, k):
      return a * pow( public_key.g, k, public_key.nsq) % public_key.nsq


def homomorphic_mult_constant(public_key, a, k):
        return pow(a, k, public_key.nsq)
'''