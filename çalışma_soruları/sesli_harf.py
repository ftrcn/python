# -*- coding: cp1254 -*-
#!/usr/bin/python
def sesli_harf():
    a=raw_input("Bir  cümle  giriniz:")
    x="aeiouAEOU"
    b=0
    for i in a:
        if i in x:
            b=b+1
            
        else:
            pass
    print b
