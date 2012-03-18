# -*- coding: cp1254 -*-
#!/usr/bin/python
def basamak_degeri_toplami(a):
    b=str(a)
    x=0
    for i in b:
        if int(i)>5:
            x=x+int(i)
    print x
