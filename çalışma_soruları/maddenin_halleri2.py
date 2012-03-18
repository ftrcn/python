# -*- coding: cp1254 -*-
#!/usr/bin/python
def maddenin_halleri():
    a=input("sıcaklık değeri  giriniz:")
    if a<=0:
        print "madde katıdır."

    elif a>0 and a<100:
        print "maddenin sıvıdır."

    elif a>=100:
        print "madde gazdır."
