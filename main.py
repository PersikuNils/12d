mala=float(input("Ievadi kvadrāta malas garumu>5 cm: "))

if mala>=5:
  kvadrats=mala*mala
  kvadrats1=(mala+5)*(mala+5)
  procenti=int((kvadrats/kvadrats1)*100)
  iznakums=str(procenti)+"%"
  print(kvadrats)
  print(kvadrats1)
  print(iznakums)
