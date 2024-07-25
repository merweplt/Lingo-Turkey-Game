import socket
import random
from colorama import Fore, Style

def kelime_sec(kelime_dosyasi):
    with open(kelime_dosyasi, "r", encoding="utf-8") as dosya:
        kelimeler = dosya.readlines()
        return random.choice(kelimeler).strip()  # Satır sonunda yer alan karakterlerini kaldırma işlemi

def main():
    server_ip = "127.0.0.1"
    server_port = 4337
    kelime_dosyasi = "kelimeler.txt"
    word = kelime_sec(kelime_dosyasi)
    max_attempts = 5
    current_attempts = 0

    # Sunucu soketi oluşturmak 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print("Sunucu dinleniyor...")

    # İstemci bağlantısını kabul etmek
    client_socket, client_address = server_socket.accept()
    print("İstemci bağlandı:", client_address)
    # İlk tahmini göndermek
    initial_guess = word[0] + '*' * (len(word) - 1)  # Sadece ilk harf ve diğer harfler için '*'
    client_socket.send(initial_guess.encode())

    # Oyun
    while current_attempts < max_attempts:
        # İstemciden tahmini al
        guess = client_socket.recv(1024).decode()

        # Tahmin doğruysa tebrik et ve döngüyü sonlandır
        if guess.upper() == word.upper():
            client_socket.send("Tebrikler".encode())
            break
         # Tahmin hakkı tükendiğinde veya doğru cevap verildiğinde bağlantıyı kapat
        elif current_attempts == max_attempts-1:
            client_socket.send(f"Bilemediniz, kelime buydu:{word}".encode())
            print("Sunucu: Bilemediniz")  # İstemciye gönderilen mesajı sunucu tarafında da ekrana yazdır
            break
        else:
            # Tahmin yanlışsa doğru tahmin edilen harfleri gönder
            current_attempts += 1
            if len(guess) != len(word):
                client_socket.send("Hatalı tahmin. Kelime {} harften oluşmalı.".format(len(word)).encode())
            else:
                response = ""
                for i in range(len(word)):
                    if guess[i].upper() == word[i].upper():
                        response += Fore.GREEN + guess[i] + Style.RESET_ALL  # Doğru harf yeşil renkte yazdırmak
                    elif guess[i].upper() in word.upper():
                        response += Fore.RED + guess[i].lower() + Style.RESET_ALL  # Yanlış yerdeki harf küçük ve kırmızı renkte yazdırmak
                    else:
                        response += "*"
                client_socket.send(response.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

