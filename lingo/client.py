import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 4337
    max_attempts = 5

    # Sunucuya bağlanmak
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Sunucudan ilk tahminin doğru sırayla alınma işlemi
    initial_response = client_socket.recv(1024).decode()   
    print("Sunucu: ", initial_response)

    # Oyun 
    attempts = 0
    while attempts < max_attempts:
        guess = input("Tahmininizi girin: ").upper()  # Kullanıcıdan tahmini alma
        client_socket.send(guess.encode())            # Tahmini sunucuya gönderme

        response = client_socket.recv(1024).decode()   # Sunucudan cevap alma
        print("Sunucu: ", response)                   # Cevabı ekrana yazdırma

        # Oyun sonlanıyor mu kontrol etme işlemi
        if response == "Tebrikler" or response == "Bilemediniz" or "Bilemediniz" in response:
            break

        attempts += 1

    client_socket.close()

if __name__ == "__main__":
    main()