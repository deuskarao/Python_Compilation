

kitaplar = [[45623, "Python", "Mustafa", "Başer", 23],
            [99878, "Linux Ağ Servisleri", "Mustafa", "Başer", 26],
            [98938, "İşletim Sistemleri", "Ali", "Saatçi", 17],
            [98947, "PHP ve AJAX", "Haydar", "Tuna", 25],
            [98947, "PHP ve PSG", "Halil", "Tuna", 24]]

# [kitapNo,kitapAdi,yazarAdi,yazarSoyadi,fiyat]

while True:
    print("""
######################
   ARAMA ÇEŞİTLERİ
----------------------
1)Kitap adı ile arama
2)Yazar adı ile arama
3)Yazar soyadı ile arama
4)Fiyat filtresi ile arama
5)Çıkış
----------------------
#######################
    """)
    aramaTipi = input("Arama stili giriniz: ")
    if aramaTipi == "1":
        while True:
            kitapAdi = input("Kitap adı giriniz: ").lower()
            if kitapAdi == "q":
                break
            elif kitapAdi.replace(" ", "").isalpha():
                varMi = False
                for b in kitaplar:
                    if kitapAdi in b[1].lower():
                        varMi = True
                        print(f"""
                    ___________________
                    Kitabın adı: {b[1]}
                    Yazar adı: {b[2] + " " + b[3]}
                    Fiyat: {b[-1]} TL
                    ___________________\n
                        """)
                if (not varMi):
                    print("[!]-> Kitap bulunamadı.\n")
            else:
                print("[!]-> Lütfen kitap adını düzgün giriniz.\n")
    elif aramaTipi == "2":
        while True:
            yazarAd = input("Yazar adı giriniz: ").lower()
            if yazarAd == "q":
                break
            elif yazarAd.replace(" ", "").isalpha():
                varMi = False
                for a in kitaplar:
                    if yazarAd in a[2].lower():
                        varMi = True
                        print(f"""
                    _______________________
                    Yazar: {a[2] + " " + a[3]}
                    Kitap adı : {a[1]}
                    Fiyat: {a[-1]} TL
                    _______________________
                        """)
                if (not varMi):
                    print(f"[!]-> {yazarAd} adına sahip bir yazar bulunamadı.\n")
            else:
                print("[!]-> Lütfen yazar adını düzgün girin.\n")
    elif aramaTipi == "3":
        while True:
            ySoyad = input("Yazar soyadı girin (Çıkmak için q) : ").lower()
            if ySoyad == "q":
                break
            elif ySoyad.replace(" ", "").isalpha():
                varMi = False
                for s in kitaplar:
                    if ySoyad in s[3].lower():
                        varMi = True
                        print(f"""\n
                    ---------------------
                    Kitap adı: {s[1]}
                    Yazar: {s[2] + " " + s[3]}
                    Fiyatı: {s[-1]} TL
                    ---------------------\n
                        """)
                if (not varMi):
                    print(f"[!]-> {ySoyad} soyadına sahip bir yazar bulunamadı.\n")
            else:
                print("[!]-> Yazar soyadını lütfen doğru biçimde girin.")
    elif aramaTipi == "4":
        while True:
            fiyat = input("Fiyat giriniz: ")
            if fiyat == "q":
                break
            elif fiyat.isnumeric():
                fiyat = int(fiyat)
                olanKitapBilgileri = []
                for u in kitaplar:
                    if u[-1] <= fiyat:
                        olanKitapBilgileri.append([u[-1], u[1], u[2] + " " + u[3]])
                olanKitapBilgileri.sort()
                if (len(olanKitapBilgileri) == 0):
                    print("[!]-> Bu fiyata kitap bulunamadı.\n")
                for x in olanKitapBilgileri:
                    print(f"""
                ----------------------
                Kitap adı: {x[1]}
                Yazar: {x[-1]}
                Fiyat: {x[0]}
                ----------------------\n
                    """)
            else:
                print("[!]-> Lütfen düzgün formatta bir fiyat giriniz.\n")
    elif aramaTipi == "5":
        print("""
        -------------------
          Program kapandı
          İyi Günler.
        -------------------
              """)
        break
    else:
        print("[!]-> Lütfen geçerli bir seçenek girin.\n")
