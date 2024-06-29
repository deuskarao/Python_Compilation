import random

kontrol = 0

alphabet = [chr(value) for value in range(97, 123)]

while True:
    yeniOyun = input("\nBaşlayalım mı? [e/h] -> ").strip().lower() if (kontrol) else input(
        "Tekrar oynayalım mı? [e/h] -> ").strip().lower()
    if yeniOyun == "e":
        kontrol = 0
        kelimeler = ["klavye", "mouse", "ekran", "anakart"]
        kelime = random.choice(kelimeler).lower()
        oyunList = ["*" for i in kelime]
        konumlar = [*range(0, len(kelime))]
        can = 0
        farklıHarfler = ""
        for x in kelime:
            if x not in farklıHarfler:
                farklıHarfler += x
                can += 1
        while (len(konumlar) != 1):
            print(f"""
        _____________________
          ADAM ASMACA OYUNU
        #####################
        Çıkış: q
        Kelime: {oyunList}
        Can: {can}
        ______________________
            """)
            tahmin = input("Tahmin giriniz: ").strip().lower()
            if tahmin == "q":
                print("Çıkış yapıldı.")
                break
            elif tahmin not in alphabet:
                print("\n[!]- Lütfen sadece bir harf giriniz -[!]\n")

            elif tahmin != kelime:
                if len(tahmin) > 1:
                    print("\n[!]- Lütfen sadece bir harf giriniz -[!]\n")
                else:
                    if tahmin in kelime:
                        for (indeks, karakter) in enumerate(kelime):
                            if tahmin == karakter:
                                oyunList[indeks] = tahmin
                                if indeks in konumlar: konumlar.remove(indeks)
                    else:
                        print("Yanlış tahmin :(")
                        can -= 1
                        if can == 0:
                            print("\n>>> KAYBETTİNİZ <<<\n")
                            break
                        konum = random.choice(konumlar)
                        oyunList[konum] = kelime[konum]
                        konumlar.remove(konum)
            else:
                print("\n>>> KAZANDINIZ <<<\n")
                break
        else:
            print(f"\n\nKelimemiz: {oyunList}")
            sonTahmin = input("Kelime tahmininizi alalım: ").strip().lower()
            if sonTahmin == kelime:
                print("\n>>> KAZANDINIZ <<<\n")
            else:
                print("\n>>> KAYBETTİNİZ <<<\n")
    elif yeniOyun == "h":
        print("Oyun kapandı.")
        break
    else:
        print("Lütfen sadece e veya h giriniz")