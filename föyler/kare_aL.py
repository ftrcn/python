import doctest
def kare_aL(sayi):
    
    """
    Bu bir doctest ornegidir.
    >>> kare_aL(2)
    4
    >>> kare_aL(0)
    0
    >>> kare_aL(-4)
    16
    """
    return (sayi * sayi)
doctest.testmod()
