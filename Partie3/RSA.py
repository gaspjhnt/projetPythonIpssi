# ---------------------------------------------------------------------------------------
# -- Import 
# 
# >>> pip install cryptography
# ---------------------------------------------------------------------------------------
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
# -------------------------------------------------------


# ---------------------------------------------------------------------------------------
# -- Functions
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
def generateKeys( ):
    """
    Generates a pair of RSA private and public keys.

    Returns:
        tuple: A tuple containing the private key and the public key.
    """
    
    vPrivateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend( )
    )
    
    vPublicKey = vPrivateKey.public_key( )
    
    return vPrivateKey, vPublicKey
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
def cipher( inPublicKey:object, inMsg:str ):
    """
    Encrypts the input message using the provided public key.

    Parameters:
    inPublicKey (object): The public key used for encryption.
    inMsg (str): The message to be encrypted.

    Returns:
    bytes: The encrypted message.
    """
    
    vMsgOut = inPublicKey.encrypt(
        inMsg.encode( ),
        padding.OAEP(
            mgf=padding.MGF1( algorithm=hashes.SHA256( ) ),
            algorithm=hashes.SHA256( ),
            label=None
        )
    )
    return vMsgOut.hex( ).upper( )
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
def decipher( vPrivateKey:object, inMsg:str ):
    """
    Deciphers the given message using the private key.

    Parameters:
    vPrivateKey (object): The private key used for decryption.
    inMsg (bytes): The encrypted message to be deciphered.

    Returns:
    str: The deciphered message.
    """
    
    vMsg = bytes.fromhex( inMsg )
    
    vDecipheredMsg = vPrivateKey.decrypt(
        vMsg,
        padding.OAEP(
            mgf=padding.MGF1( algorithm=hashes.SHA256( ) ),
            algorithm=hashes.SHA256( ),
            label=None
        )
    )
    
    return vDecipheredMsg.decode( )
# ---------------------------------------------------------------------------------------
