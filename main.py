import os
import json

def check_veri(dosya_adi):
    if os.path.exists(dosya_adi):
        print("Dosya mevcut.")
    else:
        print("Dosya mevcut değil. Oluşturuluyor...")
        try:
            with open(dosya_adi, "w") as dosya:
                dosya.write("empty")  # Dosyaya "empty" yaz
                print("Dosya oluşturuldu ve içine 'empty' yazıldı:", dosya_adi)
        except Exception as hata:
            print("Dosya oluşturulurken bir hata oluştu:", hata)

# Kullanım örneği
check_veri("veri.json")

def degeri_oku(degisken_adi):
    try:
        with open("veri.json", "r") as dosya:
            dosya_icerigi = dosya.read().strip()  # Dosyanın içeriğini oku ve başındaki ve sonundaki boşlukları temizle
            if dosya_icerigi == "empty":
                return None  # Dosya içeriği "empty" ise None döndür
            else:
                veri = json.loads(dosya_icerigi)  # Dosya içeriğini JSON olarak yükle
                return veri.get(degisken_adi)
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return None

def degeri_guncelle(degisken_adi, yeni_deger):
    try:
        with open("veri.json", "r+") as dosya:
            dosya_icerigi = dosya.read().strip()  # Dosyanın içeriğini oku ve başındaki ve sonundaki boşlukları temizle
            if dosya_icerigi == "empty":
                dosya.seek(0)  # Dosyanın başına git
                dosya.truncate()  # Dosyanın içeriğini sil
                dosya.write("{}")  # Boş bir JSON objesi yaz
                dosya_icerigi = "{}"  # Dosya içeriğini güncelle
            veri = json.loads(dosya_icerigi)  # Dosya içeriğini JSON olarak yükle
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
