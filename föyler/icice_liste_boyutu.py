def liste_boyutu(liste):
    x=0
    y=0
    z=0
    for  i in liste:
        if  type(i)==type([]):
            x=x+len(i)
            
        elif type(i)==type(" "):
            y=y+len(i)
        elif type(i)==type(int(i)):
            z=1
            
    
    print x,y,z
