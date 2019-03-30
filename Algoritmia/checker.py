#!/usr/bin/env python3

"""Check correctness of assignment"""

import sys
import string
import filecmp

def main():
    """Check correctness of assignment"""
    original = open(sys.argv[1])
    sent = open(sys.argv[2])
    #noisy = open(sys.argv[3])
    result = open(sys.argv[4])

    indomain = True
    counter = 0
    byte = sent.read(1)
    while byte:
        if byte not in string.ascii_uppercase + string.digits + string.whitespace:
            indomain = False
        counter += 1
        byte = sent.read(1)

    if not indomain:
        print("Not in domain")
        sys.exit(1)

    counter2 = 0
    byte = original.read(1)
    while byte:
        counter2 += 1
        byte = original.read(1)

    print("Increment ", end='')
    print(float(counter)/float(counter2), end='')

    result_line = result.readlines()
    result_line = result_line[0].strip()
    print(' ' + result_line)
    #print(sys.argv[2], sys.argv[3])
    #print(filecmp.cmp(sys.argv[2], sys.argv[3]))
    if (filecmp.cmp(sys.argv[2], sys.argv[3],shallow=False) and result_line == 'OK') or \
     (not filecmp.cmp(sys.argv[2], sys.argv[3], shallow=False) and result_line == 'KO'):
        sys.exit(0)
    else:
        print("Not detected")
        sys.exit(1)

if __name__ == "__main__":
    main()
