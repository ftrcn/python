# -*- coding: cp1254 -*-
#!/usr/bin/python
def string_liste2(liste):
    a=""
    for i in liste:
        if type(i)==type(str(i)):
            a=a+i
        elif type(i)==type(int(i)):
            a=a+str(i)
    return a
