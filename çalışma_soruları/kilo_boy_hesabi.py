# -*- coding: cp1254 -*-
#!/usr/bin/python
def vucut():
    float(vucut_agirligi)=input("Lütfen kilonuzu(kg) giriniz:")
    float(boy_uzunlugu)=input("Lütfen boy uzunluğunuzu(cm) giriniz:")
    a= float(vucut_agirligi)
    b=float(boy_uzunlugu)

    boy_karesi=(b/100)**2
    endeks=a/boy_karesi

    if endeks<19:
        print "zayıfsınız.Kilo almanız gerek."

    elif endeks<=25:
        print "değerleriniz normal,formdasınız."

    elif endeks<=29:
        print "şişmansınız.Diyet yapmanız gerek."

    elif endeks>29:
        print "çok şişmansınız.eee  artık  siz  düşünün."
    
