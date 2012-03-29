# -*- coding: cp1254 -*-
#!/usr/bin/python
def en_ic_topla(liste):
    sum=0
    for i in  liste:
        if type(i)==type([]):
            sum=sum + en_ic_topla(i)
        else:
            sum=sum+i
    return sum


