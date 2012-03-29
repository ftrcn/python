# -*- coding: cp1254 -*-
#!/usr/bin/python
def max_min( sayi ):
    sayimiz = str( sayi )
    maksimum = ""
    minimum = ""
    rakam = 9
    while rakam >= 0:
        for i in sayimiz :
            if int(i) == rakam :
                maksimum += str(i)
        rakam -= 1
    for i in range(len(maksimum)):
        minimum += maksimum[len(maksimum)-i-1]
    print "max = ",maksimum ,"\n min  = ", minimum
