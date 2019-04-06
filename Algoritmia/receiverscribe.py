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
        caracter = ord(byte)%8
        vector.append(caracter)
        byte=byte2
        posicio+=1
        byte2 = inputfile.read(1)
    
    suma_comprovacio = suma(vector)
    byte=inputfile.read(1)

    sum_string = []
    sum_moduls = 0

    # Calcules la suma
    while byte != ' ':
        sum_moduls += ord(byte)-ord('0')
        byte = inputfile.read(1)

    # Llegeixes els bytes de la suma
    while byte:
        sum_string.append(byte)
        byte = inputfile.read(1)
    sum_string = ''.join(sum_string[1:])
    sum_string = int(sum_string)

    print(suma_comprovacio, file=sys.stderr)
    print(sum_string, file=sys.stderr)

    if suma_comprovacio == sum_string and sum_string != sum_moduls:
        print('OK', file=sys.stderr)
        print('OK', file=outputfile)
        print("S'ha produit un canvi en els caràcters afegits")
    elif suma_comprovacio == sum_string:
        print('OK', file=sys.stderr)
        print('OK', file=outputfile)
    else:
        print('KO', file=sys.stderr)
        print('KO', file=outputfile)


if __name__ == "__main__":
    main()