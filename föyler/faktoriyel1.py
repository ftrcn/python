import doctest
def faktoriyeL(x):
  """
  >>> faktoriyeL(9)
  362880
  >>> faktoriyeL(4)
  24
  >>> faktoriyeL(1)
  1
  >>> faktoriyeL(0)
  1
  >>> faktoriyeL(-8)
  Negatif tamsayilarin faktoriyel hesaplamasi yapilamaz.
  """

  sayi=1
  if x>=0:
    while x>0:
      sayi=sayi*x
      x=x-1
    print sayi

  else:
    print "negatif tamsayilarin faktoriyel hesaplamasi yapilamaz."

  
      
           
doctest.testmod()
