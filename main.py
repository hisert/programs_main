import os
import json
import socket
import threading

class TCPClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip  # Sunucu IP adresi
        self.server_port = server_port  # Sunucu port numarası
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            print("Bağlantı başarılı.")
            # Bağlantı başarılı olduktan sonra mesaj alma işlemini başlat
            self.receive_messages()
        except Exception as e:
            print("Bağlantı hatası:", e)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                print("Gelen mesaj:", message)
            except Exception as e:
                print("Mesaj alma hatası:", e)
                break

    def send_message(self, message):
        try:
            self.client_socket.sendall(message.encode("utf-8"))
        except Exception as e:
            print("Mesaj gönderme hatası:", e)

    def close_connection(self):
        try:
            self.client_socket.close()
            print("Bağlantı kapatıldı.")
        except Exception as e:
            print("Bağlantı kapatma hatası:", e)

# Örnek kullanım
server_ip = input("Sunucu IP adresini girin: ")
server_port = int(input("Sunucu portunu girin: "))

client = TCPClient(server_ip, server_port)
client.connect()

# Bağlantıdan sonra kullanıcıdan mesaj alıp, gönderme işlemini gerçekleştiriyoruz
while True:
    message = input("Göndermek istediğiniz mesajı yazın (Çıkmak için q): ")
    if message.lower() == "q":
        client.close_connection()
        break
    client.send_message(message)

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

check_veri("veri.json")
#deger = degeri_oku(secim)
#degeri_guncelle(secim, yeni_deger)
