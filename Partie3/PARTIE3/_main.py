# ---------------------------------------------------------------------------------------
# -- Import 
# ---------------------------------------------------------------------------------------
import random as rd

import Substitution as s
import Affine as a
import RSA as r
# ---------------------------------------------------------------------------------------

gMsg = "The hardest choices require the strongest wills."

# ---------------------------------------------------------------------------------------
# -- Substitution algorithm
# ---------------------------------------------------------------------------------------
print( ">>> Substitution algorithm <<<" )
vKey = rd.choice( [ -1, 1 ] ) * rd.randint( 1, 25 )

print( f"Message to cipher: {gMsg}")
print( f"Key: {vKey}")

# -- Cipher algorithm
vCipheredMsg = s.cipher( gMsg, vKey )
print( f"Ciphered message: {vCipheredMsg}")

# -- Decipher algorithm
vDecipheredMsg = s.decipher( vCipheredMsg, vKey )
print( f"Deciphered message: {vDecipheredMsg}")
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# -- Substitution algorithm
# ---------------------------------------------------------------------------------------
print( "\n>>> Affine algorithm <<<" )
vKey = ( rd.choice( [ 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 ] ), rd.randint( 0, 100 ) )

print( f"Message to cipher: {gMsg}")
print( f"Key: {vKey}")

# -- Cipher algorithm
vCipheredMsg = a.cipher( gMsg, vKey )
print( f"Ciphered message: {vCipheredMsg}")

# -- Decipher algorithm
vDecipheredMsg = a.decipher( vCipheredMsg, vKey )
print( f"Deciphered message: {vDecipheredMsg}")
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# -- RSA algorithm
# ---------------------------------------------------------------------------------------
print( "\n>>> RSA algorithm <<<" )
# Générer les clés
vPrivateKey, vPublicKey = r.generateKeys()

print( f"Message to cipher: {gMsg}")

# -- Cipher algorithm
vCipheredMsg = r.cipher( vPublicKey, gMsg )
print( f"Ciphered message: {vCipheredMsg}")

# -- Decipher algorithm
vDecipheredMsg = r.decipher( vPrivateKey, vCipheredMsg )
print( f"Deciphered message: {vDecipheredMsg}")
# ---------------------------------------------------------------------------------------
