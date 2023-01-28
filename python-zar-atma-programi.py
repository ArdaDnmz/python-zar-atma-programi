program = False

while program == False:
    import random
    x = input("Kaç yüzlü zar atmak istiyorsun?\n")
    sayı = random.randint(1,int(x))
    print("Sonuç:", sayı)
    program = False
