# -*- coding: cp1254 -*-
#!/usr/bin/python
def en_kisa_keLime(cumle):
    k=cumle.split()
    kelime=k[0]
    uzunluk=len(k[0])
    for  i in  range(len(k)):
        if (len(k[i]))<=len(kelime):
            kelime=k[i]
            uzunluk=len(k[i])
        else:
            pass
    print "en kisa kelime:",kelime,"\n uzunluk:",uzunluk
    
