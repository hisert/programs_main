import socket

# Dosya adı
dosya_adi = "kayitlar.txt"

def kayit_oku():
    try:
        with open(dosya_adi, "r") as dosya:
            for line in dosya:
                print("Kaydedilen mesaj:", line.strip())
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı.")

def kayit_ekle(mesaj):
    with open(dosya_adi, "w") as dosya:
        dosya.write(mesaj + "\n")
        print("Yeni mesaj kaydedildi:", mesaj)

def main():
    # Sunucu adresi ve port numarası
    server = "192.168.11.216"
    port = 12345

    # Kayıtları oku
    kayit_oku()

    # Sunucuya bağlan
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server, port))
        print("Sunucuya bağlandı:", server, port)
    except Exception as e:
        print("Bağlantı hatası:", e)
        return

    # Sunucudan mesaj al ve konsola yazdır
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            print("Sunucudan gelen mesaj:", message)
            # Kaydı dosyaya ekle
            kayit_ekle(message.decode())
    except Exception as e:
        print("Mesaj alınırken hata oluştu:", e)

    # Bağlantıyı kapat
    client_socket.close()
    print("Bağlantı kapatıldı")

if __name__ == "__main__":
    main()
