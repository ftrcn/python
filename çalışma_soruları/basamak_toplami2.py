# -*- coding: cp1254 -*-
#!/usr/bin/python
def  basamak_toplami(n):
    a=0
    sayi=str(n)
    for i in sayi:
        if int(i)!=0 and int(i)!=5:
        
            a=a+int(i)
    print a
