import socket

def main():
    # Sunucu adresi ve port numarası
    server = "192.168.11.216"
    port = 12345

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
            print("Sunucudan gelen mesaj:", message.decode())
    except Exception as e:
        print("Mesaj alınırken hata oluştu:", e)

    # Bağlantıyı kapat
    client_socket.close()
    print("Bağlantı kapatıldı")

if __name__ == "__main__":
    main()
