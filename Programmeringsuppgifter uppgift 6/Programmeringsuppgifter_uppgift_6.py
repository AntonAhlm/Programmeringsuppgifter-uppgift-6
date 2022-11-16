ruta=" "*50
print(ruta,"+","-"*16,"+")
print(ruta,"|  Te21C           |")
print(ruta,"|  Anton Ahlm      |")
print(ruta,"+","-"*16,"+\n\n")


tid=int(input("Hur manga minuter? "))
if tid%60==0:
   print(int(tid/60),"h")
else:
    print(int(tid/60),"h",tid % 60,"min") 
