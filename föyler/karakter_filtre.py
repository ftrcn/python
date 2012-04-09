def karakter_filtre(dosya_adi,karakter):
     a=open(dosya_adi)
     for i in a:
        satir=i.strip()
        if karakter not in a:
            print  satir
        else:
            pass
