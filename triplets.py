

def triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if (a**2+b**2) == c**2:
                return (a, b, c)

print(triplet())

def pythagorean_triplet_dickson():
 for r in range(1,1000):
  for s in range(1,r):
   if ((r**2)/2)%s == 0:
    t = (r**2/2)/s
    if r+s+r+t+r+t+s == 1000:
     return ((r+s),(r+t),(r+t+s))

#Printing the result
#print (pythagorean_triplet_dickson())