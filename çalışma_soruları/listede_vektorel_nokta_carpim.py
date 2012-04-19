# -*- coding: cp1254 -*-
#!/usr/bin/python
def  vektor_nokta_carpimi(a,b):
    #a ve b birer listedir.
    listem=[]
    for i in range(len(a)):
        listem.append(a[i]*b[i])
        son=sum(listem)
    print "nokta çarpımı=",son




