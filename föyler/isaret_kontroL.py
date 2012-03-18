# -*- coding: cp1254 -*-
#!/usr/bin/python
import doctest
def isaret_kontroL(sayi_1,sayi_2):
    """
    >>> isaret_kontroL(9,4)
    1
    >>> isaret_kontroL(6,0)
    0
    >>> isaret_kontroL(3,-13)
    -1
    """

    carpim=sayi_1*sayi_2
    if carpim>0:
        return 1
    elif carpim<0:
        return -1
    elif carpim==0:
        return 0

doctest.testmod()
    
