import socket
import threading

IP_target = socket.gethostbyname(input("Masukkan ip/domain : "))
PORT_AWAL = int(input("Masukkan Port : "))
PORT_AKHIR = int(input("Masukkan Port akhir : ")) + 1

print(f"Memindai {IP_target}")

# 1. TUGAS PEKERJA: Mengecek SATU port saja
def panggil_port(port):
    kabel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    kabel.settimeout(1)
    hasil_ketukan = kabel.connect_ex((IP_target, port))
    if hasil_ketukan == 0:
        print(f"BINGO! port {port} terbuka")
    kabel.close()

# 2. MANDOR: Mencetak banyak pekerja (thread) menggunakan looping
# Perhatikan bahwa baris 'for' ini disejajarkan ke kiri (di luar fungsi)
for port in range(PORT_AWAL, PORT_AKHIR):
    t = threading.Thread(target=panggil_port, args=(port,))
    t.start()

print("\nScan Selesai!")