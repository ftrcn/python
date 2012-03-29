# -*- coding: cp1254 -*-
#!/usr/bin/python
def aLfabetik_artan(kelime):
    yeni=list(kelime)
    x="abcdefghiklmnoprstvyz"
    for i in x:
        a=yeni.sort()
        if yeni==a:
            return True
        else:
            return  False
