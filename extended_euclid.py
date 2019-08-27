# COMP90043 Cryptography and Security
# Assignment 1, Semester 2 2019
# Question 2
#
# Name: Emmanuel Macario <macarioe>
# Student Number: 831659
# Date: 21/08/19

def extended_gcd(a, b):
    """
    Computes the GCD of a and b by
    extended Euclid's algorithm
    :param a: first integer
    :param b: second integer
    :return: None
    """
    s = 0
    t = 1
    r = b
    old_s = 1
    old_t = 0
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    print("Bezout coefficients: {:d} {:d}".format(old_s, old_t))
    print("Greatest common divisor:", old_r)
    print("Quotient by the gcd: {:d} {:d}".format(t, s))


def multiplicative_inverse(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    # Should consider the case when a < n
    s = 0
    r = b
    old_s = 1
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if b != 0:
        bezout_t = (old_r - old_s * a) // b
    else:
        bezout_t = 0

    print("Bezout coefficients: {:d} {:d}".format(old_s, bezout_t))
    print("Greatest common divisor:", old_r)

    return old_s


if __name__ == "__main__":
    a = 10**100 - 24**13
    b = 26**45
    extended_gcd(a, b)



    print("\n")
    multiplicative_inverse(a, b)

    print('\n')
    multiplicative_inverse(1473, 1562)
