import socket
import sys

def main(server, port):
    # Sunucuya bağlan
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server, port))
        print("Sunucuya bağlandı:", server, port)
    except Exception as e:
        print("Bağlantı hatası:", e)
        sys.exit(1)

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
    if len(sys.argv) != 3:
        print("Kullanım: python client.py <server> <port>")
        sys.exit(1)

    server = sys.argv[1]
    port = int(sys.argv[2])
    main(server, port)
