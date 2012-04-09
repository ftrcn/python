def listenin_buyugu(liste):
    a=liste[0]
    for  i  in range(len(liste)):
        if type(liste[i])==type([]):
            if liste[i]>=a:
               a=listenin_buyugu(liste[i])
            else:
                pass
            
        else:
            if  liste[i]>=a:
                a=liste[i]
            else:
                pass
    return a
        
        
