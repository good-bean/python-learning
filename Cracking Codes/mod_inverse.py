import gcd

def findModInverse(a, m):
    if gcd.gcd(a, m) != 1:
        return None # No mod inverse if a & m aren't relatively prime.
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        print('q = %s' % (q))
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        print('v1 = %s : v2 = %s : v3 = %s : u1 = %s : u2 = %s : u3 = %s' % (v1, v2, v3, u1, u2, u3))
    return u1 % m
