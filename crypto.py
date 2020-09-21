# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypt_dummy = []

    for i in ciphertext:
        if ord(ciphertext[i]) < ord('A') or ord(ciphertext[i]) > ord('Z'):
            return "Incorrect Input"
        encrypt_dummy.append(ord(ciphertext(i)))
        encrypt_dummy[i] + offset
        encrypt_dummy[i] = chr(encrypt_dummy[i]) 
    
    return ''.join(encrypt_dummy)

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    encrypt_dummy = []

    if ord(ciphertext[i]) < ord('A') or ord(ciphertext[i]) > ord('Z'):
            return "Incorrect Input"

    for i in ciphertext:
        encrypt_dummy.append(ord(ciphertext(i)))
        encrypt_dummy[i] = encrypt_dummy[i] - offset
        encrypt_dummy[i] = chr(encrypt_dummy[i])
    return ''.join(encrypt_dummy)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    print encrypt_caesar("MARVIN", 1)
    

if __name__ == "__main__":
    main()
