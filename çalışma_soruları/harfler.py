# -*- coding: cp1254 -*-
#!/usr/bin/python
def sesli_harf():
    a=raw_input("Bir  cümle  giriniz:")
    x="aeiouAEOU"
    y="bcdfghklmnprstvyz"
    b=0
    c=0
    m=0
    for i in a:
        if i in x:
            b=b+1

            
        elif i in y:
            c=c+1
        elif i!=b and i!=c:
            m=m+1
    print b,c,m
