#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes and checks
the hash byte"""

import sys

def suma(vector):
    suma = 0
    for x in vector:
        suma+=x
    return suma

def main():
    """Reads from stdin and outputs to stdout the same sequence of bytes and checks the hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = []
    byte = inputfile.read(1)
    byte2 = inputfile.read(1)
    posicio=2
    while byte != ' ' or byte2 != ' ':
        caracter = ord(byte)%9
        vector.append(caracter)
        byte=byte2
        posicio+=1
        byte2 = inputfile.read(1)
    
    suma_comprovacio = suma(vector)
    byte=byte2
    byte=inputfile.read(1)
    #print(byte)

    sum_string = []
    sum_final = []
    sum_moduls = 0
    while byte:
        if byte==' ':
            byte=inputfile.read(1)
            #print(byte)
            while byte:
                sum_string.append(byte)
                #print(sum_final)
                byte=inputfile.read(1)
                #print(byte)
        else:
            sum_moduls+=int(ord(byte)-ord('0'))
            byte=inputfile.read(1)
            #print(byte)

    sum_final = ''.join(map(str, sum_string))
    resultat = int(sum_final)
        
    #while byte!=' ':
     #   byte2=inputfile.read(1)
    #byte2=inputfile.read(1)
    #while byte:
     #   sum_final = []
      #  sum_final.append('byte')
       # byte=inputfile.read(1)
    
    #print(suma_comprovacio)
    #print(resultat)
    #print(resultat)
    #print(sum_moduls)
    if suma_comprovacio == resultat and resultat != sum_moduls:
        print('OK', file=outputfile)
        print("S'ha produit un canvi en els caràcters afegits")
    elif suma_comprovacio == resultat:
        print('OK', file=outputfile)
    else:
        print('KO', file=outputfile)
    #print(byte2)
    #vector_final = operacio_array(vector)
    
   # for x in vector_final:
       # sum_final += x
    #checker = sum_final
    #checker=chr(ord('A')+(checker%25))
        
   # if checker == ultim_caracter:
   #     print('OK', file=outputfile)
    #else:
     #   print('KO', file=outputfile)


if __name__ == "__main__":
    main()