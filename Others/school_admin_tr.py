import time

ogrenciler = []
ogrNo = 0
while True:
    print(f"""
##########################################
#        |_____________________|         #
#        |  OKUL İDARE PANELİ  |         #
#        | 1)Öğrenci ekleme    |         #
#        | 2)Öğrenci silme     |         #
#        | 3)Öğrenci listesi   |         #
#        |_____________________|         #
#-> Çıkış için "ç" tuşu kullanılabilir <-#
##########################################
    """)
    islem = input("İşlem numarası giriniz: ")
    if islem.lower() == "ç":
        break
    elif (islem == "1"):
        kosul1 = True
        while True:
            ogrAdi = input("Öğrenci adını giriniz: ").strip()
            if ogrAdi.lower() == "ç":
                kosul1 = False
                break
            elif not(not ogrAdi.replace(" ", "").isalpha()) and not (len(ogrAdi) < 3):
                print("[!]-> Lütfen geçerli bir öğrenci adı giriniz.\n")
                continue
            kosul1 = True
            ogrAdi = ogrAdi.title()
            break
        kosul2 = False
        while kosul1:
            ogrSoyadi = input("Öğrenci soyadını giriniz: ").strip()
            if ogrSoyadi.lower() == "ç":
                break
            elif (not ogrSoyadi.replace(" ", "").isalpha()) or (len(ogrSoyadi) < 2):
                print("[!]-> Lütfen geçerli bir ogrenci soyadı giriniz.\n")
                continue
            kosul2 = True
            ogrSoyadi = ogrSoyadi.title()
            break
        kosul3 = False
        while kosul2:
            veliNo = input("Öğrenci veli telefon numarasını giriniz +90 ").strip()
            if veliNo.lower() == "ç":
                break
            elif ((not veliNo.isnumeric()) or (len(veliNo) < 10) or (len(veliNo) == 10 and veliNo[0] == "0") or (
                    len(veliNo) > 11)) or (len(veliNo) == 11 and veliNo[0] != "0"):
                print("[!]-> Lütfen geçerli formatta bir telefon numarası girin.\n")
                continue
            elif (len(veliNo) == 10):
                veliNo = "0" + veliNo
            kosul3 = True
            break
        if kosul3:
            ogrNo += 1
            print(f"Öğrencimize okul numarası olarak {ogrNo} verilmiştir.\n")
            print("Öğrenci ekleniyor....")
            time.sleep(2)
            ogrenci = [ogrAdi, ogrSoyadi, ogrNo, veliNo]
            ogrenciler.append(ogrenci)
            print("[*]-> Öğrenci kayıt edildi. <-[*]")
    elif (islem == "2"):
        while True:
            if (len(ogrenciler) == 0):
                print("[*]-> Kayıtlı öğrenci bulunamadı.\n")
                break
            else:
                ogrenciNo = input("Silinecek öğrencinin okul numarasını giriniz: ")
                if ogrenciNo == "ç":
                    break
                elif (not ogrenciNo.isnumeric()):
                    print("[!]-> Öğrenci okul numarasını doğru girdiğinizden emin olun. <-[!]\n")
                else:
                    ogrenciNo = int(ogrenciNo)
                    indeks = 0
                    for n in ogrenciler:
                        if ogrenciNo == n[2]:
                            print(f"""
                        ________________________
                        Öğrenci adı: {n[0]}
                        Öğrenci soyadı: {n[1]}
                        Öğrenci no: {n[2]}
                        ------------------------
                        Veli no: {n[-1]}
                            """)
                            silinsinMi = input("Öğrenci silinsin mi? [e/h]: ")
                            if silinsinMi == "e":
                                print("Öğrenci siliniyor.....")
                                time.sleep(3)
                                ogrenciler.pop(indeks)
                                print("[*]-> Öğrenci silindi <-[*]")
                                break
                            elif silinsinMi == "h":
                                break
                            else:
                                print("[!]-> Lütfen e veya h giriniz <-[!]")
                        indeks += 1
    elif (islem == "3"):
        if len(ogrenciler) == 0:
            print("\n[!]-> Kayıtlarda öğrenci bulunamadı. <-[!]")
        else:
            ogrenciler.sort()
            for bilgi in ogrenciler:
                print(f"""
            _____________________
            Öğrenci adı: {bilgi[0]}
            Öğrenci soyadı: {bilgi[1]}
            Öğrenci no: {bilgi[2]}
            ---------------------
            Veli no: {bilgi[-1]}
                \n""")
            print("[ Öğrenciler isim sırasına göre sıralandı ]")
            menuyeDon = input("Panele dönmek için herhangi bir tuşa basınız: ")
    else:
        print("\n[!]-> Lütfen geçerli bir işlem giriniz <-[!]")
