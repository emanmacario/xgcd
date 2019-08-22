import numpy as np
import string
import textwrap
import math


m = 4

test_ciphertext = """!LPUMYAIJ?.MPA.DVRFUTNRUZYEFM?QVKJTOBTDRIAN!?SLQBKESZO
SFRAAWYPI.VBOLLMWAWEMQ.JYBOITGNJRIFYGEGIBC?RB?UN?MORI"""

p_map = {}
for n, l in enumerate(string.ascii_uppercase):
    p_map[l] = n
p_map[','] = 26
p_map['.'] = 27
p_map['?'] = 28
p_map['!'] = 29
p_map[' '] = 30

c_map = {c: p for p, c in p_map.items()}

plaintexts = ['CTRL', 'CAPS', 'HOME', 'PGUP']
ciphertexts = ['HGPP', 'HOFL', 'TTSI', 'DACR']




def convert_to_matrix(texts):
    """
    :param texts:
    :return: matrix
    """
    matrix = []
    for text in texts:
        row = [p_map[p] for p in text]
        matrix.append(row)
    return np.array(matrix, dtype=np.int64)



def encrypt(plaintext, key):
    """
    :param plaintext:
    :param key:
    :return:
    """
    p = np.array([p_map[p] for p in plaintext], dtype=np.int64)
    c = np.dot(p, key) % 31
    return ''.join([c_map[round(n) % 31] for n in c])


def decrypt(ciphertext, key):
    """
    :param ciphertext:
    :param key:
    :return:
    """
    c = np.array([p_map[c] for c in ciphertext], dtype=np.int64)
    p = np.dot(c, np.linalg.inv(key) % 31) % 31
    print(p)
    return ''.join([c_map[round(n) % 31] for n in p])


def main():
    #print(len(ciphertext))
    #print(string.ascii_uppercase)
    #print(p_map)
    X = convert_to_matrix(plaintexts)
    Y = convert_to_matrix(ciphertexts)

    K = np.dot(np.linalg.inv(X), Y) % 31
    print(encrypt('CTRL', K))
    print(encrypt('CAPS', K))
    print(encrypt('HOME', K))
    print(encrypt('PGUP', K))


    """
    test_plaintext = ""
    for ciphertext in textwrap.wrap(test_ciphertext, m):
        test_plaintext += decrypt(ciphertext, K)

    print(test_plaintext)
    """

    for ciphertext in ciphertexts:
        print(decrypt(ciphertext, K))



if __name__ == "__main__":
    main()
