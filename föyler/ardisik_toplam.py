# -*- coding: cp1254 -*-
#!/usr/bin/python
def  ardisik_toplam(n):
     x=0
     if  n>0 and type(n)==type(int(n)):
          while n:
            x=x+n
            n=n-1
          print x
        
     else:
        print "Lütfen pozitif bir tamsayi giriniz."


