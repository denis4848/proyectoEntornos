# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:24:29 2021

@author: DenisAndreiGuimpuSte
"""
import math

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
        
def areaCuadrado():
        cont=0
        maxx=int(input("Cantidad de cuadrados que deseas"))
        print("\n CUADRADO")
        for i in range(1,maxx*2+1):
            if(i%2==0):
                cont+=1
                cuadrado=i*i
                print("el area del cuadrado",cont, "de lado ",i, "es ", cuadrado)
            
def areaDeVariosCirculos():
        maxx=int(input("Cantidad de circulos que deseas"))
        cont=0
        for i in range(1,maxx*2+1):
            if(i%2==0):
                cont+=1
                circulo=((i)**2)*math.pi
                print("el area del circulo",cont ,"de radio ",i*2, "es ", round(circulo,2))

def areaTriangulo():
        b=float(input("Dame la base: "))
        a=float(input("Dame la altura: "))
        area=b*a/2
        print("el area del triangulo es:", area)

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
    5.- area de los n primeros circulos pares
    6.- modulo 
    7.- cociente 
    8.- exponente 
    9.- area primeros n cuadrados pares
    10.- area triangulo
    
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
    elif(x==9): #area cuadrado
        areaCuadrado()
    elif(x==5): #area circulo
        areaDeVariosCirculos()
    elif(x==10): #area triangulo
        areaTriangulo()
