# -*- coding: cp1254 -*-
#!/usr/bin/python
def vucut():
    float(vucut_agirligi)=input("L�tfen kilonuzu(kg) giriniz:")
    float(boy_uzunlugu)=input("L�tfen boy uzunlu�unuzu(cm) giriniz:")
    a= float(vucut_agirligi)
    b=float(boy_uzunlugu)

    boy_karesi=(b/100)**2
    endeks=a/boy_karesi

    if endeks<19:
        print "zay�fs�n�z.Kilo alman�z gerek."

    elif endeks<=25:
        print "de�erleriniz normal,formdas�n�z."

    elif endeks<=29:
        print "�i�mans�n�z.Diyet yapman�z gerek."

    elif endeks>29:
        print "�ok �i�mans�n�z.eee  art�k  siz  d���n�n."
    
