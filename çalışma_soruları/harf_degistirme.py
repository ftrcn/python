# -*- coding: cp1254 -*-
#!/usr/bin/python
def dizgi_harf_degistir(string,harfin_sirasi,harf):
    a=""
    b=0
    harf=str(harf)
    string=str(string)
    for i in string:
        b+=1
        if b==harfin_sirasi:
            a+=harf
        else:
            a+=i
    print a
