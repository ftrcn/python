# -*- coding: cp1254 -*-
#!/usr/bin/python
def harf_disi_karakter_sil():
    a=raw_input("Bir  cümle  giriniz:")
    x="aeiouAEOUbcdfghklmnprstvyzBCDFGHKLMNPRSTVYZ"
    y=" "
    for i in a:
        if i in x:
            y=y+i
        else:
            pass
    print y
