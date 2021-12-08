# Feladat: Írj programot ingatlanhirdetések kezelésére!

# A hirdetések adatai az 'ingatlanok.json' fájlban vannak tárolva.
# Egy ingatlanhoz az alábbi adatok tartoznak:
# településnév (city)
# cím (address)
# ár - MFt (price)
# alapterület (area)
# szobaszám (rooms)

# A program indításkor kérdezze meg a felhasználótól, hogy új hirdetést
# szeretne feladni vagy keresni szeretne.

# Új hirdetés feladásánál kérje be az adatait és mentse bele a fájlba.
# (A megadott adatok formátumát nem kell ellenőrizni.)

# Ingatlankeresésnél kínáljon fel szűrési lehetőségeket.
# A szűrések a main()-ben vannak részletezve.
# Minden szűrés után írja ki, hány hirdetés felel meg a feltételeknek.
# Végül, a megmaradt hirdetések közül írja ki az adatait annak, amelyiknek
# a legalacsonyabb a négyzetméterenkénti ára.
# Vagy azt, hogy "Nincs a szűréseknek megfelelő hirdetés."

# A fájlból olvasás, szűrések, és a legjobb kiválasztása legyenek külön
# függvényekben implementálva. Ezt a vizsgáztató helyben fogja ellenőrizni.


def main():
    print("1: Új hirdetés feladása")
    print("2: Hirdetések szűrése")
    input("Válasszon egy menüpontot: ")
    
    # Új hirdetés
    input("Település neve: ")
    input("Utca, házszám: ")
    input("Eladási ár (MFt): ")
    input("Alapterület: ")
    input("Szobák száma: ")
    
    # Szűrések
    db = 0
    # TODO
    print(db, "hirdetés van az adatbázisban")
    input("Adja meg a kívánt település nevét, vagy nyomjon Enter-t ezen szűrés kihagyásához: ")
    # TODO
    print(db, "hirdetés felel meg a szűrési feltételeknek")
    input("Adja meg a kívánt minimális szobaszámot, vagy nyomjon Enter-t ezen szűrés kihagyásához: ")
    # TODO
    print(db, "hirdetés felel meg a szűrési feltételeknek")
    input("Adja meg a kívánt maximális szobaszámot, vagy nyomjon Enter-t ezen szűrés kihagyásához: ")
    # TODO
    print(db, "hirdetés felel meg a szűrési feltételeknek")
    
    print("A legjobb négyzetméterenkénti árú ingatlan:")
    # TODO
    print("Nincs a szűréseknek megfelelő hirdetés.")

if __name__ == '__main__':
    main()
