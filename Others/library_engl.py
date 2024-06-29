
Books = [   [45623, "Python", "Mustafa", "Başer", 23],
            [99878, "Linux Ağ Servisleri", "Mustafa", "Başer", 26],
            [98938, "İşletim Sistemleri", "Ali", "Saatçi", 17],
            [98947, "PHP ve AJAX", "Haydar", "Tuna", 25],
            [98947, "PHP ve PSG", "Halil", "Tuna", 24]]

# [bookNo,bookname,authname,authsur,price]


while True:
    print("""
#############################
|       SEARCH TYPES        |
| ------------------------- | 
|   1) Book   Name          |
|   2) Author Name          |
|   3) Author Surname       |
|   4) Price  Filter        |
|   5) Exit                 |  #k.adı sıfre modulu getır sonra kitap eklet herkes ekleyemesin
|   A) Add a  Book          |
| _________________________ |
#############################
    """)

    seType = input("Enter the Search Type: ")
    if seType == "1":
        while True:
            bookName = input("Enter the name of the book: ")
            if bookName == "q" or "Q":
                print("\nProgram Ended")
                break


