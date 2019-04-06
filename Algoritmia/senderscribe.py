#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes plus a
hash byte"""

import sys


def suma(vector):
    """ Descripció suma """
    res = 0
    for valor in vector:
        res += valor
    return res


def main_text(byte, vector, inputfile, outputfile):
    """ Holaaa """
    while byte:
        print(byte, end='', file=outputfile)
        caracter = ord(byte) % 8
        vector.append(caracter)
        byte = inputfile.read(1)


def primer_check(vector, outputfile):
    """ Comentari """
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


def main_text_r(byte, vector):
    """ Holaa """
    if byte:
        print(byte, end='', file=sys.stdout)
        vector.append(ord(byte) % 8)
        main_text_r(sys.stdin.read(1), vector)


def recursive_main():
    """ Comentaris"""
    outputfile = sys.stdout

    vector = []
    byte = sys.stdin.read(1)
    main_text_r(byte, vector)

    #TO-DO: recurive valor
    print(' ', end='', file=outputfile)
    print(' ', end='', file=outputfile)
    for valor in vector:
        print(valor, end='', file=outputfile)

    print(' ', end='',
          file=outputfile)
    print(suma(vector), end='', file=outputfile)


if __name__ == "__main__":
    main()
