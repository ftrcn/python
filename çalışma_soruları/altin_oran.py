# -*- coding: cp1254 -*-
#!/usr/bin/python
def altin_oran(n):
    a=0
    b=1
    while(n>0):
        a, b = b, a+b
        n=n-1
    print float(b)/a
