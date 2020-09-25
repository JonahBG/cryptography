# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypt_dummy = []



    for i in plaintext:
        if ord(i) < ord('A') or ord(i) > ord('Z'):
            return "Incorrect Input"
        encrypt_dummy.append(chr(ord('A') + ((ord(i) - ord('A') + offset) % 26)))

    return ''.join(encrypt_dummy)

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    encrypt_dummy = []

    for i in ciphertext:
        if ord(i) < ord('A') or ord(i) > ord('Z'):
            return "Incorrect Input"
        encrypt_dummy.append(chr(ord('A') + ((ord(i) - ord('A') - offset) % 26)))

    return ''.join(encrypt_dummy)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypt_dummy = []
    for i in range(len(plaintext)):

        if ord(plaintext[i]) < ord('A') or ord(plaintext[i]) > ord('Z'):
            return "Incorrect Input"
        offset = ord(keyword[i % len(keyword)]) - ord('A')
        encrypt_dummy.append(chr(ord('A') + ((ord(plaintext[i]) - ord('A') + offset) % 26)))
    return ''.join(encrypt_dummy)

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    encrypt_dummy = []
    for i in range(len(ciphertext)):

        if ord(ciphertext[i]) < ord('A') or ord(ciphertext[i]) > ord('Z'):
            return "Incorrect Input"
        offset = ord(keyword[i % len(keyword)]) - ord('A')
        encrypt_dummy.append(chr(ord('A') + ((ord(ciphertext[i]) - ord('A') - offset) % 26)))
    return ''.join(encrypt_dummy)


# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    
    W = ()
    W.append(random.randint(1,101))
    total = W[0]
    for i in range (0,n):
        W.append(random.randint(total + 1, 2 * total))
        total + W[i]
    Q = random.randint(total + 1, 2 * total)
    R = 0
    while true:
        R = random.randint(2, Q-1)
        if math.gcd(R,Q) == 1:
            false
    return [W,Q,R]

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    B = ()
    for i in range (0,8):
        b.append(R * W[i] % Q)

    return B

def bits_to_byte(bits):
    #take a list of 0 and 1 length 8 and turn it into a number between 0 and 255

def byte_to_bits(byte):
    #take a number between 0 and 255, returns a list of 0 and 1 of length 8
    returnList = [0,0,0,0,0,0,0,0]
    i = 0
    while byte >= 0 and i < 8:

        if 2 ** (7 -i) <= byte:
            returnList[i] = 1
            byte = byte - 2 ** (7-i)
        i = i + 1
    return returnList
# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass
    
# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    print (byte_to_bits(155))
    

if __name__ == "__main__":
    main()
