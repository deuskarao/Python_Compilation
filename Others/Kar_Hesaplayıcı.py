
def satis_fiyati(satir):

	satir = satir[:-1]

	liste = satir.split(",")

	masraf = int(liste[1])/100*20

	vergi = int(liste[1])/100*18

	kar = int(liste[1])/100*25

	son_satis_fiyati = int(liste[1])+masraf+vergi+kar

	return "Ürün: " + liste[0] + " -- Satis Fiyat1: " + str(son_satis_fiyati) + "\n"


with open("Maliyetler.txt", "r", encoding="utf-8") as file:
	
	for i in file:
		urunler = []
		urunler.append = [satis_fiyati(i)]

with open("Satis_Fiyatlari.txt", "a", encoding="utf-8") as satis:
	satis.writelines(urunler)
