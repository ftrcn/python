# -*- coding: cp1254 -*-
#!/usr/bin/python
def  vize_finaL_notu():
    a=input("vize notunu giriniz:")
    b=input("final notunu giriniz:")

    x=a*(40/100.0)+b*(60/100.0)
    if x>=60:
        print "Finalden geçti."
    elif x<60:
        print "büte kaldı."
        
        c=input("büt notunuzu giriniz:")
        y=a*(40/100.0)+c*(60/100.0)

        if y>=60:
            print "bütten geçtiniz."
        else:
            print "bütten kaldınız."
