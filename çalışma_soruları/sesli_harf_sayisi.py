# -*- coding: cp1254 -*-
#!/usr/bin/python
def  sesli_harf_sayisi(s):
    sesli="aeiouAEIOU"
    a=0
    for i in s:
        if i in sesli:
            a=a+1
    print a
