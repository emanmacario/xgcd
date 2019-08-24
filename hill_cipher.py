import numpy as np
import string
import textwrap
import math

from extended_euclid import multiplicative_inverse

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


def convert_to_row(text):
    """
    :param text:
    :return:
    """
    return np.array([p_map[p] for p in text], dtype=np.int64)


def convert_to_matrix(texts):
    """
    :param texts:
    :return: matrix
    """
    matrix = []
    for text in texts:
        row = convert_to_row(text)
        matrix.append(row)
    return np.array(matrix, dtype=np.int64)


def encrypt(plaintext, key):
    """
    :param plaintext:
    :param key:
    :return:
    """
    p = convert_to_row(plaintext)
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

    K = np.dot(np.linalg.inv(X) % 31, Y) % 31
    print(K)
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


def sub_matrix(matrix, i, j):
    """
    Return sub-matrix formed by deleting jth
    row and ith column
    :param matrix:
    :param i:
    :param j:
    :return:
    """
    tmp = np.delete(matrix, j, 0)
    return np.delete(tmp, i, 1)


def sub_determinant(matrix, i, j, mod=31):
    """
    Returns sub-determinant formed by deleting the
    jth row and ith column of A, mod 31
    :param matrix:
    :param i: column index
    :param j: row index
    :param mod: mod (optional)
    :return: sub-determinant
    """
    sm = sub_matrix(matrix, i, j)
    return int(round(np.linalg.det(sm))) % mod


if __name__ == "__main__":
    K = np.array([[17, 17, 5],
                  [21, 18, 21],
                  [2, 2, 19]])
    """
    sm = sub_matrix(K, 1, 2)
    print(sm)
    dsm = sub_determinant(K, 1, 2)
    print(dsm)
    exit(1)
    """


    print(K)
    det_K = int(round(np.linalg.det(K))) % 26
    print("Determinant of K = ", det_K)
    m_inv = multiplicative_inverse(det_K, 26) % 26
    print("(det K)^-1 mod 26 = ", m_inv)

    inverse = [[] for _ in range(3)]
    print(inverse)
    for a in range(3):
        for b in range(3):
            inverse[a].append(m_inv * (-1)**(a+b) * sub_determinant(K, a, b, 26))

    inverse = np.array(inverse) % 26
    print("K^-1 = \n", inverse)
    print("K * K^-1 = \n", np.dot(K, inverse) % 26)




