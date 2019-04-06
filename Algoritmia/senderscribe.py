#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes plus a
hash byte"""

import sys

def suma(vector):
    suma = 0
    for x in vector:
        suma+=x
    return suma

def main():
    """Reads from stdin and outputs to stdout the same sequence of bytes plus a hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    #checker = 0
    vector = []
    #caracters_passats = []
    byte = inputfile.read(1)
    while byte:
        #caracters_passats.append(byte)
        print(byte, end='', file=outputfile)
        caracter = ord(byte)%8  #AIXI O MODUL 8????????????????????????????????
        vector.append(caracter)
        byte = inputfile.read(1)
    
    #caracters_passats.append(' ')
    print(' ', end='', file=outputfile)  
    print(' ', end='', file=outputfile)   #posem dos espais per a poder-ho diferenciar de lsespais que hi ha al missatge que ens passen
    for x in vector:
        print(x, end='', file=outputfile)

    print(' ', end='', file=outputfile)   #utilitzem aquest espai per a separar els caràcters afegits del resultat de la suma d'aquests
    suma_comprovacio = suma(vector)
    print(suma_comprovacio, end='', file=outputfile)

def recursive_main():
    """ Comentaris"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = []
    byte = sys.stdin.read(1)
    recursive(byte, vector)

    print(' ', end='', file=outputfile)
    print(' ', end='',
          file=outputfile)  # posem dos espais per a poder-ho diferenciar de lsespais que hi ha al missatge que ens passen
    for x in vector:
        print(x, end='', file=outputfile)

    print(' ', end='',
          file=outputfile)  # utilitzem aquest espai per a separar els caràcters afegits del resultat de la suma d'aquests
    print(suma(vector), end='', file=outputfile)

def recursive(byte, vector):
    """ Holaa """
    if byte:
        print(byte, end='', file=sys.stdout)
        vector.append(ord(byte) % 8)
        recursive(sys.stdin.read(1), vector)



if __name__ == "__main__":
    main()