import os
import json

def check_veri(dosya_adi):
    if os.path.exists(dosya_adi):
        print("Dosya mevcut.")
    else:
        print("Dosya mevcut değil. Oluşturuluyor...")
        try:
            with open(dosya_adi, "w") as dosya:
                print("Dosya oluşturuldu:", dosya_adi)
        except Exception as hata:
            print("Dosya oluşturulurken bir hata oluştu:", hata)

# Kullanım örneği
check_veri("veri.json")

def degeri_oku(degisken_adi):
    try:
        with open("veri.json", "r") as dosya:
            veri = json.load(dosya)
            return veri.get(degisken_adi)
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return None

def degeri_guncelle(degisken_adi, yeni_deger):
    try:
        with open("veri.json", "r") as dosya:
            veri = json.load(dosya)
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return

    veri[degisken_adi] = yeni_deger

    with open("veri.json", "w") as dosya:
        json.dump(veri, dosya)

# Değeri okuma
secim = input("Hangi değeri okumak istiyorsunuz? (string_1 veya string_2): ")
deger = degeri_oku(secim)
if deger is not None:
    print(f"Okunan değer ({secim}):", deger)

# Değeri güncelleme
secim = input("Hangi değeri güncellemek istiyorsunuz? (string_1 veya string_2): ")
yeni_deger = input("Yeni değer: ")
degeri_guncelle(secim, yeni_deger)

# Güncellenmiş değeri okuma
secim = input("Hangi değeri okumak istiyorsunuz? (string_1 veya string_2): ")
deger = degeri_oku(secim)
if deger is not None:
    print(f"Güncellenmiş değer ({secim}):", deger)
