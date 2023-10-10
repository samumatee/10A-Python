"""
ev1 = int(input("adj meg az evszam1-et: "))
ev2 = int(input("adj meg az evszam2-t: "))

honap1 = int(input("adj meg az honap1-et: "))
honap2 = int(input("adj meg az honap2-t: "))

nap1 = int(input("adj meg az nap1-et: "))
nap2 = int(input("adj meg az nap2-t: "))
def napok_kozott_eltelt(ev1, ho1, nap1, ev2, ho2, nap2): 
    adat = 0
    ev = 0
    honap = 0
    nap = 0

    napok1 = ev1 * 365 + ho1 * 30 + nap1
    napok2 = ev2 * 362 + ho2 * 30 + nap2
    eltelt_napok = napok2 - napok1
    
    adat.append(eltelt_napok)

    while adat > 365: 
        adat -= 365
        ev += 1
    
    while adat > 30: 
        adat -= 30
        honap += 1
    
    return adat


napok_kozott_eltelt()
"""
"""
def napok_kozott_eltelt(): 
    datum1 = input("Adja meg az első dátumot [hh:nn]: ")
    datum2 = input("Adja meg az masodik dátumot [hh:nn]: ")

    ev1, ho1 = map(int, datum1.split(":"))
    ev2, ho2 = map(int, datum2.split(":"))

    eltelt_napok = (ho2 - ho1) + ((ev2 - ev1) * 365)

    return eltelt_napok

eltelt_napok = napok_kozott_eltelt()

if eltelt_napok is not None: 
    print(f"eltelt napok szama: {eltelt_napok}")
"""

def napok_szama(datum1, datum2):
    honap1, napszam1 = map(int, datum1.split(":"))
    honap2, napszam2 = map(int, datum2.split(":"))

    napok_honaponkent = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if napszam1 < napszam2: 
        napszam1, napszam2 = napszam2, napszam1

    napok_kulombsege = sum(napok_honaponkent[h] for h in range(honap1, honap2)) - napszam1 + napszam2

    return napok_kulombsege

datum1 = input("Datum: ")
datum2 = input("Datum: ")

napok_kulombsege = napok_szama(datum1,datum2)

print(f"Eltelt napok szama: {napok_kulombsege}")
