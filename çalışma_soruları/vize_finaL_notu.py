# -*- coding: cp1254 -*-
#!/usr/bin/python
def  vize_finaL_notu():
    a=input("vize notunu giriniz:")
    b=input("final notunu giriniz:")

    x=a*(40/100.0)+b*(60/100.0)
    if x>=60:
        print "Finalden ge�ti."
    elif x<60:
        print "b�te kald�."
        
        c=input("b�t notunuzu giriniz:")
        y=a*(40/100.0)+c*(60/100.0)

        if y>=60:
            print "b�tten ge�tiniz."
        else:
            print "b�tten kald�n�z."
