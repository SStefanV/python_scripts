def gcd(a, b):
    '''
        Functie pentru a calcula
        Cel mai mare divizor comun. 
    '''
    old_g = a
    g = b   
    while(g  != 0):
        old_g, g = g, old_g % g
    return old_g
print(gcd(32, 8))
