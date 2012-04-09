def string_icindekiler(string):
    a=0
    b=0
    c=0
    x="aeouiAEOUÝ"
    y="bcdfghjklmnprstvyz"
    z="1234567890"
    for i in string:
        if i in x:
            a=a+1
        elif i in y:
            b=b+1
        elif i in z:
            c=c+1
    print "sesli sayýsý:",a,"\nsessiz sayýsý:",b,"\nsayý sayýsý:",c,"\nkarakter sayisi:",a+b
    
            
            
