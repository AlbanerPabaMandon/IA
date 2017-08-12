import random

tablero=[]
DIMENSIONES=15

#Establece la matriz vacia para el tablero
def establecer():
    global tablero
    
    for i in range(DIMENSIONES):
        tablero.append([])
        for j in range(DIMENSIONES):
            tablero[i].append(None)
    for x in range(DIMENSIONES):
        for y in range(DIMENSIONES):
            tablero[x][y]="_"
            
#Imprime el tablero            
def imprimir():
    global tablero
    
    for y in range(DIMENSIONES):
        print str([i[y] for i in tablero])+"\n"
    

#Ejecuta las funciones necesarias para la simulacion
def simular():
    #Posiciones de la dama aleatoria
    x=random.randint(0, DIMENSIONES-1)
    y=random.randint(0, DIMENSIONES-1) 
    
    #Dama aleatoria distingida por la letra R
    posicionar(x,y,"R")
    
    iterar(x,y)
    
    print "Damas Colocadas: "+str(contar())+" \n \n "
                
#Algoritmo para colocar las damas
def iterar(x,y):
    global tablero
    
    y=(y+3)%DIMENSIONES
    
    for i in range(DIMENSIONES):
        x=(x+1)%DIMENSIONES
        for j in range(DIMENSIONES):
            if(tablero[x][(y+j)%DIMENSIONES]=="_"):
                posicionar(x,(y+j)%DIMENSIONES,"Q")#str(i))
                j=DIMENSIONES+1
                y=(((y+j)%DIMENSIONES)+3)%DIMENSIONES

                              
#Posiciona y define los ataques de una dama    
def posicionar(x,y,letra):
    global tablero
    
    for i in range(DIMENSIONES):
        #Ataques en cruz
        tablero[x][i]="*"
        tablero[i][y]="*"
        
        #Ataques en diagonal
        if((x+i)<DIMENSIONES and (y+i)<DIMENSIONES):
            tablero[(x+i)][(y+i)]="*"
        if((x-i)>=0 and (y+i)<DIMENSIONES):
            tablero[(x-i)][(y+i)]="*"
        if((x+i)<DIMENSIONES and (y-i)>=0):
            tablero[(x+i)][(y-i)]="*"
        if((x-i)>=0 and (y-i)>=0):
            tablero[(x-i)][(y-i)]="*"
            
    #Coloca la ficha en la posicion indicaca
    tablero[x][y]=letra
        
    
#Cuenta cuantas damas hay en el tablero
def contar():
    global tablero
    
    counter=0
    for x in range(DIMENSIONES):
        for y in range(DIMENSIONES):
            if(tablero[x][y]!="_" and tablero[x][y]!="*"):
                counter=counter+1
    return counter
        

establecer()
simular()
imprimir()
