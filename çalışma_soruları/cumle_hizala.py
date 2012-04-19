# -*- coding: cp1254 -*-
#!/usr/bin/python
def cumle_hizala(cumle,yon,x):
    if yon=="sola":
        a=cumle+" "*x
    elif yon=="ortala":
        a=" "*(x/2)+cumle
    elif yon=="saga":
        a=" "*x+cumle
    print a
