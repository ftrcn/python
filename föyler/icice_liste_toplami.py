def liste_toplami(liste):
    x=0
    for  i in liste:
        if  type(i)==type([]):
            x=x+liste_toplami(i)
            
        else:
            x=x+i
    
    return x
