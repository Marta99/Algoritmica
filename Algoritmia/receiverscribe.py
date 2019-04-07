#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes and checks
the hash byte"""

import sys

def sumatori_vector(vector):
    """ Suma tots els valors del vector i retorna el seu resultat"""
    result = 0
    for valor in vector:
        result += ord(valor) % 10
    return result

def llegir_resultat_suma(inputfile):
    """ Llegeix un dels sumatoris del text"""
    valor_sumatori = []
    byte = inputfile.read(1)
    while byte and byte != ' ':
        if byte.isdigit():
            valor_sumatori.append(byte)
        byte = inputfile.read(1)
    valor_sumatori = ''.join(valor_sumatori)
    return int(valor_sumatori)

def valor_diferent(valor1, valor2, valor3, valor4):
    """ Retorna el valor diferent dels 4 """
    if valor1 not in (valor2, valor3):
        return valor1
    if valor2 not in (valor1, valor2):
        return valor2
    if valor3 not in (valor1, valor4):
        return valor3
    return valor4

def main():
    """Reads from stdin and outputs to stdout the same sequence of bytes and checks the hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = []
    byte = inputfile.read(1)
    byte2 = inputfile.read(1)
    posicio = 2
    while byte != ' ' or byte2 != ' ':
        vector.append(byte)
        byte = byte2
        posicio += 1
        byte2 = inputfile.read(1)

    suma_text = sumatori_vector(vector)

    byte = inputfile.read(1)
    suma_checker_text = 0
    posicio_vector = 0
    trobada_diferencia = False

    # Calcules la suma del checker
    while byte != ' ':
        caracter = (ord(byte) - ord('0'))
        if caracter != ord(vector[posicio_vector]) % 10:
            posicio_errata = posicio_vector
            num_caracter_error = caracter
            trobada_diferencia = True
        suma_checker_text += caracter
        byte = inputfile.read(1)
        posicio_vector += 1

    valor_primer_sumatori = llegir_resultat_suma(inputfile)
    valor_segon_sumatori = llegir_resultat_suma(inputfile)

    if not trobada_diferencia and suma_text == suma_checker_text and\
            valor_primer_sumatori == suma_checker_text and\
            valor_segon_sumatori == suma_checker_text:
        print('OK', file=outputfile)
    else:
        if trobada_diferencia and valor_primer_sumatori == suma_checker_text:
            print('KO', file=outputfile)
            print(str(posicio_errata) + ' ' + chr(num_caracter_error + ord('0')), file=outputfile)
        else:
            print('KO', file=outputfile)

def sumatori_vector_r(vector):
    """ Suma tots els valors del vector i retorna el seu resultat"""
    if vector == []:
        return 0
    return ord(vector[0]) + sumatori_vector_r(vector[1:])

def llegir_resultat_suma_r(inputfile, byte, sumatori):
    """ Llegeix un dels sumatoris del text"""
    if not byte or byte == ' ':
        return int(''.join(sumatori))
    sumatori.append(byte)
    return llegir_resultat_suma_r(inputfile, inputfile.read(1), sumatori)

def llegir_text_r(byte1, byte2, vector, posicio):
    """ Llegeix el text """
    if byte1 != ' ' or byte2 != ' ':
        vector.append(byte1)
        return llegir_text_r(byte2, sys.stdin.read(1), vector, posicio + 1)
    return vector

def suma_checker_r(byte, resultat, posicio, valors_derror, vector):
    """ Suma el primer checker i mira si hi ha un error"""
    if byte == ' ':
        return resultat, valors_derror
    caracter = ord(byte) - ord('0')
    if caracter != ord(vector[posicio]) % 10:
        valors_derror[0] = True
        valors_derror[1] = posicio
        valors_derror[2] = caracter
    return suma_checker_r(sys.stdin.read(1), resultat + caracter, posicio + 1, \
                          valors_derror, vector)


def main_r():
    """Reads from stdin and outputs to stdout the same sequence of bytes and checks the hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = llegir_text_r(inputfile.read(1), inputfile.read(1), [], 2)

    suma_text = sumatori_vector(vector)
    byte = inputfile.read(1)

    # Calcules la suma del checker
    suma_checker_text, trobada_diferencia, posicio_errata, num_caracter_error =\
        suma_checker_r(byte, 0, 0, [False, -1, -1], vector)

    valor_primer_sumatori = llegir_resultat_suma_r(inputfile, inputfile.read(1), [])
    valor_segon_sumatori = llegir_resultat_suma_r(inputfile, inputfile.read(1), [])

    if not trobada_diferencia and suma_text == suma_checker_text and\
            valor_primer_sumatori == suma_checker_text and\
            valor_segon_sumatori == suma_checker_text:
        print('OK', file=outputfile)
    else:
        if trobada_diferencia and valor_primer_sumatori == suma_checker_text:
            print('KO', file=outputfile)
            print(str(posicio_errata) + ' ' + chr(num_caracter_error + ord('0')), file=outputfile)
        elif trobada_diferencia:
            print('KO', file=outputfile)
            print(str(posicio_errata + len(vector)) + ' ' + chr(vector[posicio_errata] % 10), file=outputfile)
        else:
            print('KO', file=outputfile)

if __name__ == "__main__":
    main()
