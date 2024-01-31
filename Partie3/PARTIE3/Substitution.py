# ---------------------------------------------------------------------------------------
# -- Parameters
# ---------------------------------------------------------------------------------------
gLowerLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
gUpperLetter  = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T" ,"U", "V", "W", "Y", "Z"]
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# -- Functions
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
def cipher( inMsg:str, inKey:int ):
    """
    Encrypts a message using a substitution cipher. Supposed with no accent.

    Args:
        inMsg (str): The input message to be encrypted.
        inKey (int): The key used for encryption.

    Returns:
        str: The encrypted message.
    """
    global gLowerLetters, gUpperLetter
    
    vOutMsg = ""
    
    for lLetter in inMsg:
        if lLetter in gLowerLetters: # a -> z
            vNewLetter = gLowerLetters[ ( gLowerLetters.index( lLetter ) + inKey ) % 25 ]
            
        elif lLetter in gUpperLetter: # A -> Z
            vNewLetter = gUpperLetter[ ( gUpperLetter.index( lLetter ) + inKey ) % 25 ]
            
        else: # Other (space, punctuation, etc.)
            vNewLetter = lLetter
        
        vOutMsg += vNewLetter

    return vOutMsg
# ---------------------------------------------------------------------------------------
        
# ---------------------------------------------------------------------------------------
def decipher( inMsg:str, inKey:int ):
    """
    Decrypts a message using a substitution cipher. Supposed with no accent.

    Args:
        inMsg (str): The input message to be decrypted.
        inKey (int): The key used for decryption.

    Returns:
        str: The decrypted message.
    """
    global gLowerLetters, gUpperLetter
    
    vOutMsg = ""
    
    for lLetter in inMsg:
        if lLetter in gLowerLetters: # a -> z
            vNewLetter = gLowerLetters[ ( gLowerLetters.index( lLetter ) - inKey ) % 25 ]
            
        elif lLetter in gUpperLetter: # A -> Z
            vNewLetter = gUpperLetter[ ( gUpperLetter.index( lLetter ) - inKey ) % 25 ]
            
        else: # Other (space, punctuation, etc.)
            vNewLetter = lLetter
        
        vOutMsg += vNewLetter

    return vOutMsg
# ---------------------------------------------------------------------------------------