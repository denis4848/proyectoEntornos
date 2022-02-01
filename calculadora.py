# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:24:29 2021

@author: DenisAndreiGuimpuSte
"""


#definiciones////////////////////////////////////

def suma():
    n1=int(input("Dame numero 1"))
    n2=int(input("Dame numero 2"))
    print("la suma de", n1, "y", n2, "es: ", n1+n2)

def resta():
    n1=int(input("Dame numero 1"))
    n2=int(input("Dame numero 2"))
    print("la resta de", n1, "y", n2, "es: ", n1-n2)

#programa///////////////////////////////////////////

      
print("\n\t-------------\n\t-CALCULADORA-\n\t-------------\n")
x=100

while (x!=0):
    x=int(input("""
    0.- salir
    1.- suma 
    2.- resta 

    if (x==1): #suma
        suma()
    elif(x==2): #resta
        resta()
    
    Dame un numero: 
        """))