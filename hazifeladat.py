#Maximum keresés
from operator import index

szamok = [-1000, -600, -200, -500, 200, 600, 1000]

max, a = -1000, 0
indexek = 1

for i in szamok:
    print("max: ", max, "i:", i, "index: ", indexek)
    indexek += 1
    
    #Próbálkoztam vele de ez sikerült