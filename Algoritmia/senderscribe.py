#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes plus a
hash byte"""

import sys


def suma(vector):
    """ Suma tots els valors del vector i retorna el seu resultat """
    res = 0
    for valor in vector:
        res += valor
    return res


def main_text(byte, vector, inputfile, outputfile):
    """ Llegeix el text i el modul 10 del seu símbol el guarda a un vector"""
    while byte:
        print(byte, end='', file=outputfile)
        caracter = ord(byte) % 10
        vector.append(caracter)
        byte = inputfile.read(1)


def primer_check(vector, outputfile):
    """ Guarda a l'outputfile el valors del vector """
    print(' ', end='', file=outputfile)
    print(' ', end='', file=outputfile)
    for valor in vector:
        print(valor, end='', file=outputfile)


def main():
    """Reads from stdin and outputs to stdout the same sequence of bytes plus a hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = []
    main_text(inputfile.read(1), vector, inputfile, outputfile)
    primer_check(vector, outputfile)

    print(' ', end='', file=outputfile)
    resultat = suma(vector)
    print(resultat, end='', file=outputfile)
    print(' ', end='', file=outputfile)
    print(resultat, end='', file=outputfile)


def main_text_r(byte, vector):
    """ Holaa """
    if byte:
        print(byte, end='', file=sys.stdout)
        vector.append(ord(byte) % 8)
        main_text_r(sys.stdin.read(1), vector)

def primer_check_r(vector, outputfile):
    """ Guarda a l'outputfile el valors del vector """
    if vector is []:
        print(vector[0], end='', file=outputfile)
        primer_check_r(vector[1:], outputfile)


def main_r():
    """Reads from stdin and outputs to stdout the same sequence of bytes plus a hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = []
    main_text_r(inputfile.read(1), vector)
    print(' ', end='', file=outputfile)
    print(' ', end='', file=outputfile)
    primer_check_r(vector, outputfile)

    print(' ', end='', file=outputfile)
    resultat = suma(vector)
    print(resultat, end='', file=outputfile)
    print(' ', end='', file=outputfile)
    print(resultat, end='', file=outputfile)


if __name__ == "__main__":
    main()
