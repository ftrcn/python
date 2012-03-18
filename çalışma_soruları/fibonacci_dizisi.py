# -*- coding: cp1254 -*-
#!/usr/bin/python
def fibonacci_dizisi(n):
    a,b=0,1
    for i in range(n):
        print b,
        a,b =b,a+b
