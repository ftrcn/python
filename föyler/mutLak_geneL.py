# -*- coding: cp1254 -*-
#!/usr/bin/python
import math
def mutLak_geneL():
    while True:
        s = input("Karmasik sayilar icin 1,tamsayi icin 2,ondalik icin 3,cikmak 4 giriniz:" )
        if s==1 :    
            a = input("Gercel kismi giriniz:")
            b = input("sanal kismi giriniz:")
            w = math.sqrt((a**2)+(b**2))
            print "kompleks sayinin mutlak degeri:",w
        elif s==2 :
            a = input("Tamsayi giriniz:")
            if a<0 :
                t = -1*a
                print "Tamsayi mutlak degeri:",t
            else :
                print "Tamsayi mutlak degeri:",a
        elif s==3 :
            a = input("Ondalikli sayi giriniz:")
            if a<0 :
                k = -1*a
                print "Ondalikli sayinin mutlak degeri:",k
            else :
                print "Ondalikli sayinin mutlak degeri:",a
        else :
            break
