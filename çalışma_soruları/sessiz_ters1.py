# -*- coding: cp1254 -*-
#!/usr/bin/python
def sessiz_ters(a):
    sesliler="aeiouAEIOU"
    ters=""
    n=0
    for harf  in a:
        if harf in sesliler:
            ters=ters+"*"
        else:
            ters=ters+harf
        n=n+1
    while n:
        print ters[n-1],
        n=n-1
