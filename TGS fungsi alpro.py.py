import math

def main_menu():
    print("1. Hitung Panjang Persegi Panjang")
    print("2. Hitung Lebar Persegi Panjang")
    print("3. Hitung Sisi Persegi")
    print("4. Hitung Radius Lingkaran")
    print("5. Keluar")

# Mendefinisikan fungsi
def panjang_persegi_panjang(lebar=None, luas=None, keliling=None):
    if lebar and luas:
        return luas / lebar
    elif lebar and keliling:
        return (keliling - 2 * lebar) / 2
    else:
        return "Parameter tidak lengkap atau tidak valid."

def lebar_persegi_panjang(panjang=None, luas=None, keliling=None):
    if panjang and luas:
        return luas / panjang
    elif panjang and keliling:
        return (keliling - 2 * panjang) / 2
    else:
        return "Parameter tidak lengkap atau tidak valid."

def sisi_persegi(luas=None, keliling=None):
    if luas:
        return math.sqrt(luas)
    elif keliling:
        return keliling / 4
    else:
        return "Parameter tidak lengkap atau tidak valid."

def radius_lingkaran(luas=None, keliling=None):
    if luas:
        return 2 * math.sqrt(luas / math.pi)
    elif keliling:
        return keliling / math.pi
    else:
        return "Parameter tidak lengkap atau tidak valid."

def main():
    while True:
        main_menu()
        pilihan = input("Pilih salah satu nomor diatas: ")
        
        if pilihan == '1':
            lebar = float(input("Masukkan lebar (atau kosongkan jika tidak diketahui): ") or "0")
            luas = float(input("Masukkan luas (atau kosongkan jika tidak diketahui): ") or "0")
            keliling = float(input("Masukkan keliling (atau kosongkan jika tidak diketahui): ") or "0")
            result = panjang_persegi_panjang(lebar if lebar > 0 else None, luas if luas > 0 else None, keliling if keliling > 0 else None)
            print("Panjang Persegi Panjang:", result)
        
        elif pilihan == '2':
            panjang = float(input("Masukkan panjang (atau kosongkan jika tidak diketahui): ") or "0")
            luas = float(input("Masukkan luas (atau kosongkan jika tidak diketahui): ") or "0")
            keliling = float(input("Masukkan keliling (atau kosongkan jika tidak diketahui): ") or "0")
            result = lebar_persegi_panjang(panjang if panjang > 0 else None, luas if luas > 0 else None, keliling if keliling > 0 else None)
            print("Lebar Persegi Panjang:", result)
        
        elif pilihan == '3':
            luas = float(input("Masukkan luas (atau kosongkan jika tidak diketahui): ") or "0")
            keliling = float(input("Masukkan keliling (atau kosongkan jika tidak diketahui): ") or "0")
            result = sisi_persegi(luas if luas > 0 else None, keliling if keliling > 0 else None)
            print("Sisi Persegi:", result)
            
        elif pilihan == '4':
            luas = float(input("Masukkan luas (atau kosongkan jika tidak diketahui): ") or "0")
            keliling = float(input("Masukkan keliling (atau kosongkan jika tidak diketahui): ") or "0")
            result = radius_lingkaran(luas if luas > 0 else None, keliling if keliling > 0 else None)
            print("Radius Lingkaran:", result)

        elif pilihan == '5':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()