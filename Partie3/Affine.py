# ---------------------------------------------------------------------------------------
# -- Parameters
# ---------------------------------------------------------------------------------------
gLowerLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# -- Functions
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
def cipher(inMsg: str, inKey: tuple[int, int]) -> str:
    """
    Applies the Affine cipher to the input message using the provided key. Supposed with not accent

    Args:
        inMsg (str): The input message to be encrypted.
        inKey (tuple[int, int]): The key used for encryption. It consists of two integers (a, b).

    Returns:
        str: The encrypted message.

    """
    
    assert inKey[ 0 ] in [ 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 ], "Invalid key: a has to be coprime with 26"
    
    vOutMsg = ""
    vA = inKey[ 0 ]
    vB = inKey[ 1 ]

    for lLetter in inMsg:
        if lLetter.lower( ) in gLowerLetters:
            vNewLetter = gLowerLetters[ ( vA * gLowerLetters.index( lLetter.lower( ) ) + vB ) % 26 ]

            if lLetter.lower( ) == lLetter:
                vOutMsg += vNewLetter
            else:
                vOutMsg += vNewLetter.upper( )

        else:
            vOutMsg += lLetter

    return vOutMsg
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
def decipher(inMsg: str, inKey: tuple[int, int]) -> str:
    """
    Applies the Affine cipher to the input message using the provided key. Supposed with not accent
    Expected a affine function with such as f(x) = ax + b

    Args:
        inMsg (str): The input message to be encrypted.
        inKey (tuple[int, int]): The key used for encryption. It consists of two integers (a, b).

    Returns:
        str: The encrypted message.

    """
    
    # https://en.wikipedia.org/wiki/Affine_cipher
    assert inKey[ 0 ] in [ 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 ], "Invalid key: a has to be coprime with 26"

    # -- Bachet-Bézout theorem
    for lA in range( 1, 26 ):
        if ( inKey[ 0 ] * lA ) % 26 == 1:
            vA = lA
            break

    vOutMsg = ""
    vB = inKey[1]

    for lLetter in inMsg:
        if lLetter.lower( ) in gLowerLetters:
            # -- Apply affine function with letter index
            vNewLetter = gLowerLetters[ ( ( gLowerLetters.index( lLetter.lower( ) ) - vB ) * vA ) % 26 ]

            if lLetter.lower( ) == lLetter:
                vOutMsg += vNewLetter
            else:
                vOutMsg += vNewLetter.upper( )

        else:
            vOutMsg += lLetter

    return vOutMsg
# ---------------------------------------------------------------------------------------