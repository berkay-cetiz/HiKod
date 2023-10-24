ogrenciler = {
    "Ali": {"Matematik": 85, "Fizik": 70, "Kimya": 90},
    "Veli": {"Matematik": 90, "Fizik": 80, "Kimya": 75},
    "Ayse": {"Matematik": 75, "Fizik": 85, "Kimya": 95},
}
while True:
    print("1. Öğrenci bilgilerini görüntüle")
    print("2. Öğrenci notunu değiştir")
    print("3. Öğrenci notu ekle")
    print("4. Çıkış")

    secim = input("Seçiminizi yapınız: ")

    if secim == "1":
        isim = input("Öğrenci adı giriniz: ")
        if isim in ogrenciler:
            print("Öğrenci bilgileri:")
            for ders, puan in ogrenciler[isim].items():
                print(f"{ders}: {puan}")
        else:
            print(f"{isim} isimli öğrenci yok.")

    elif secim == "2":
        isim = input("Öğrenci adı giriniz: ")
        if isim in ogrenciler:
            ders = input("Ders adı giriniz: ")
            if ders in ogrenciler[isim]:
                yeni_not = input("Yeni notu giriniz: ")
                ogrenciler[isim][ders] = yeni_not
                print(f"{isim} isimli öğrencinin {ders} ders notu {yeni_not} olarak güncellendi.")
            else:
                print(f"{isim} isimli öğrencinin {ders} dersi yok.")
        else:
            print(f"{isim} isimli öğrenci yok.")

    elif secim == "3":
        isim = input("Öğrenci adı giriniz: ")
        if isim in ogrenciler:
            ders = input("Ders adı giriniz: ")
            puan = input("Notu giriniz: ")
            ogrenciler[isim][ders] = puan
            print(f"{isim} isimli öğrencinin {ders} ders notu {puan} olarak eklendi.")
        else:
            print(f"{isim} isimli öğrenci yok.")

    elif secim == "4":
        break

    else:
        print("Geçersiz seçim.")
