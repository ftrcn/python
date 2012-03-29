# -*- coding: cp1254 -*-
#!/usr/bin/python
def basamak_degeri2(n):
      a = 0
      while n:
          x = n % 10
          if x>a:
            a=x
          n = n / 10
      return a


basamak_degeri2(1294)
