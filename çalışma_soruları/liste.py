# -*- coding: cp1254 -*-
#!/usr/bin/python
def liste(n):
    liste2=[]
    
    for i in n:
        if i%2==0:
            liste2.append(0)
        
        else:
            liste2.append(1)
    print liste2
