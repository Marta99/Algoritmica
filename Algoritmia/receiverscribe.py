#!/usr/bin/env python3

"""Reads from stdin and outputs to stdout the same sequence of bytes and checks
the hash byte"""

import sys

def sumatori_vector(vector):
    """ Comentari """
    result = 0
    for valor in vector:
        result += ord(valor) % 10
    return result

def llegir_resultat_suma(inputfile):
    """ Comentari """
    valor_sumatori = []
    byte = inputfile.read(1)
    while byte and byte != ' ':
        valor_sumatori.append(byte)
        byte = inputfile.read(1)
    valor_sumatori = ''.join(valor_sumatori)
    return int(valor_sumatori)

def valor_diferent(valor1, valor2, valor3, valor4):
    if valor1 != valor2 and valor1 != valor3:
        return valor1
    elif valor1 != valor2 and valor2 != valor3:
        return valor2
    elif valor1 != valor3 and valor3 != valor4:
        return valor3
    else:
        return valor4

def main():
    """Reads from stdin and outputs to stdout the same sequence of bytes and checks the hash byte"""
    inputfile = sys.stdin
    outputfile = sys.stdout

    vector = []
    byte = inputfile.read(1)
    byte2 = inputfile.read(1)
    posicio=2
    while byte != ' ' or byte2 != ' ':
        vector.append(byte)
        byte=byte2
        posicio+=1
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

    if not trobada_diferencia and suma_text == suma_checker_text and valor_primer_sumatori == suma_checker_text and valor_segon_sumatori == suma_checker_text:
        print('OK', file=outputfile)
    else:
        if trobada_diferencia and valor_primer_sumatori == suma_checker_text:
            print('KO', file=outputfile)
            print(str(posicio_errata) + ' ' + chr(num_caracter_error + ord('0')), file=outputfile)
        else:
            print('KO', file=outputfile)


if __name__ == "__main__":
    main()