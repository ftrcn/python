# -*- coding: cp1254 -*-
#!/usr/bin/python
def fibonacci_dizisi2(n):
    a,b=0,1
    for i in range(n-1):
        a,b =b,a+b
    print b,
