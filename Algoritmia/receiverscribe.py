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
    while byte:
        if byte==' ':
            byte=inputfile.read(1)
            while byte:
                sum_string.append(byte)
                byte=inputfile.read(1)
        else:
            sum_moduls+=int(ord(byte)-ord('0'))
            byte=inputfile.read(1)

    sum_final = ''.join(map(str, sum_string))
    resultat = int(sum_final)
        

    while byte:
        print(byte, end='', file=outputfile)
        caracter = ord(byte) % 8
        vector.append(caracter)
        byte = inputfile.read(1)

    if suma_comprovacio == resultat and resultat != sum_moduls:
        print('OK', file=outputfile)
        print("S'ha produit un canvi en els caràcters afegits")
    elif suma_comprovacio == resultat:
        print('OK', file=outputfile)
    else:
        print('KO', file=outputfile)


def recursive_main():
    """Reads from stdin and outputs to stdout the same sequence of bytes and checks the hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = []
    byte = inputfile.read(1)
    byte2 = inputfile.read(1)
    posicio = 2
    while byte != ' ' or byte2 != ' ':
        caracter = ord(byte) % 8
        vector.append(caracter)
        byte = byte2
        posicio += 1
        byte2 = inputfile.read(1)

    suma_comprovacio = suma(vector)
    byte = inputfile.read(1)

    sum_string = []
    sum_moduls = 0
    while byte:
        if byte == ' ':
            byte = inputfile.read(1)
            while byte:
                sum_string.append(byte)
                byte = inputfile.read(1)
        else:
            sum_moduls += int(ord(byte) - ord('0'))
            byte = inputfile.read(1)

    sum_final = ''.join(map(str, sum_string))
    resultat = int(sum_final)

    while byte:
        print(byte, end='', file=outputfile)
        caracter = ord(byte) % 8
        vector.append(caracter)
        byte = inputfile.read(1)

    if suma_comprovacio == resultat and resultat != sum_moduls:
        print('OK', file=outputfile)
        print("S'ha produit un canvi en els caràcters afegits")
    elif suma_comprovacio == resultat:
        print('OK', file=outputfile)
    else:
        print('KO', file=outputfile)


def resursive(byte, sum_string, sum_moduls):
    """ Comentaris """
    if byte:
        if byte == ' ':
            byte = sys.stdin.read(1)
            while byte:
                sum_string.append(byte)
                byte = sys.stdin.read(1)
        else:
            sum_moduls += int(ord(byte) - ord('0'))
            byte = sys.stdin.read(1)


if __name__ == "__main__":
    main()