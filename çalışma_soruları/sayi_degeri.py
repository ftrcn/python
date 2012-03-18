# -*- coding: cp1254 -*-
#!/usr/bin/python
def sayi_degeri(n):
    sayi=str(n)
    a=sayi[0]
    for i in sayi:
        if int(i)>=int(a):
            a=int(i)
    print a
