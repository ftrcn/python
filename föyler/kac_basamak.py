# -*- coding: cp1254 -*-
#!/usr/bin/python
def  kac_basamak(a):
    x=0
    if a==0 :
       x=x+1 
       while a>0:
          a=a/10
          x=x+1
    return x
