# -*- coding: cp1254 -*-
#!/usr/bin/python
def taban_cevirme(sayi,taban):
    son=0
    a=len(sayi)
    say=a
    for i in sayi:
        say=say-1
        x=int(i)*taban**say
        son=son+x
    print son
