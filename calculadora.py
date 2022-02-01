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

def multiplicacion():
    n1=int(input("Dame numero 1"))
    n2=int(input("Dame numero 2"))
    print("la multiplicacion de", n1, "y", n2, "es: ", n1*n2)

def division():
    n1=int(input("Dame numero 1"))
    n2=int(input("Dame numero 2"))
    if(n1>n2 & n2!=0):
        print("la división de", n1, "y", n2, "es: ", n1/n2)
    if(n2==0): 
        print("No se puede dividir entre 0")
    elif(n2>n1 & n1!=0):
        print("la división de", n1, "y", n2, "es: ", n2/n1)
    if(n1==0):
        print("No se puede dividir entre 0")
def modulo():
        n1=int(input("Dame numero 1"))
        n2=int(input("Dame numero 2"))
        if(n1>n2 & n2!=0):
            print("el modulo de", n1, "y", n2, "es: ", n1%n2)
        if(n2==0):
            print("No se puede dividir entre 0")
        elif(n2>n1 & n1!=0):
            print("el modulo de", n1, "y", n2, "es: ", n2%n1)
        if(n1==0):
            print("No se puede dividir entre 0")
            
def exponente():
        n1=int(input("Dame numero 1"))
        n2=int(input("Dame numero 2"))
        print("el exponente de", n1, "y", n2, "es: ", n1**n2)

def cociente():
        n1=int(input("Dame numero 1"))
        n2=int(input("Dame numero 2"))
        print("el cociente de", n1, "y", n2, "es: ", n1//n2)
#programa///////////////////////////////////////////

      
print("\n\t-------------\n\t-CALCULADORA-\n\t-------------\n")
x=100

while (x!=0):
    x=int(input("""
    0.- salir
    1.- suma 
    2.- resta
    3.- multiplicacion 
    4.- division
    6.- modulo 
    7.- cociente 
    8.- exponente 
    Dame un numero: 
        """))

    if (x==1): #suma
        suma()
    elif(x==2): #resta
        resta()
    elif(x==3): #multiplicacion
        multiplicacion()
    elif(x==4): #division
       division()
    elif(x==6): #modulo
       modulo()
    elif(x==7): #cociente
        cociente()
    elif(x==8): #exponente
        exponente()

    
