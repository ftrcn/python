# -*- coding: cp1254 -*-
#!/usr/bin/python
import string
def cumledeki_kelime_harf_buyut(cumle):
        liste =cumle.split()
        for i in range(len(liste)):
           liste[i] = liste[i].capitalize()
           cumle_2 = string.join(liste,' ')
        print cumle_2
