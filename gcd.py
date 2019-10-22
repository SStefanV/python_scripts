def gcd(a, b):
    '''
        Functie pentru a calcula
        Cel mai mare divizor comun. 
    '''
    g = b
    old_g = a
    while(g  != 0):
        old_g, g = g, old_g % g
    return old_g
print(gcd(456, 244))
