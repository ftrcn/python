# -*- coding: cp1254 -*-
#!/usr/bin/python
import doctest

def sondan_basa_yaz(cumle):
    
    """\
    >>> sondan_basa_yaz("ondokuz mayis Universitesi")
    isetisrevinU siyam zukokno
    >>> sondan_basa_yaz("")
    l�tfen parametre olarak karalter dizisi giriniz.
    >>> sondan_basa_yaz(45)
    l�tfen parametre olarak karalter dizisi giriniz.

    """
    

    dizgi=""

    if cumle==str(cumle):
        for i in cumle[::-1]:
            dizgi+=i
        return dizgi


    else:
        print "l�tfen parametre olarak karakter dizisi giriniz."
        
    
doctest.testmod()
