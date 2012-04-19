# -*- coding: cp1254 -*-
#!/usr/bin/python
def dizgi_harf_degistir(dizgi,degistirilecek_harfin_sirasi,harf):
    a=""
    c=0
    harf=str(harf)
    dizgi=str(dizgi)
    for i in dizgi :
        c+=1
        if c==degistirilecek_harfin_sirasi:
            a+=harf
        else:
            a+=i
    print a
