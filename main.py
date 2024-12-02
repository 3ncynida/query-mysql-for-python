from koneksi import create_connection  # Modul koneksi
from list_db import list_databases           # Modul untuk daftar database
from drop_db import drop_database            # Modul untuk menghapus database
import mysql.connector

# Fungsi utama untuk menjalankan perintah
def main():
    # Membuat koneksi ke MySQL
    mydb = create_connection()

    if mydb:  # Periksa apakah koneksi berhasil
        while True:  # Loop tak terbatas
            print("\nMenu:")
            print("1. List database")
            print("2. Buat database")
            print("3. Hapus Database")
            print("ketik 'exit' untuk keluar")

            # Meminta input perintah dari pengguna
            command = input("Masukkan nomor perintah (1/2/3): ")

            if command == "1":  # List database
                list_databases()  # Memanggil fungsi dari modul list_db
            
            elif command == "2":  # Buat database
                db_name = input("Masukkan nama database yang ingin dibuat: ")
                mycursor = mydb.cursor()
                try:
                    mycursor.execute(f"CREATE DATABASE {db_name}")
                    print(f"Database '{db_name}' berhasil dibuat!")
                except mysql.connector.Error as err:
                    print(f"Error saat membuat database: {err}")
                    
            elif command == "3":  # Hapus database
                drop_database()  # Memanggil fungsi dari modul drop_db
            
            elif command.lower() == "exit":  # Keluar dari program
                print("Terima kasih! Program selesai.")
                break  # Keluar dari loop
            
            else:
                print("Perintah tidak valid. Silakan masukkan 1, 2, 3, atau 'exit'.")
        
        mydb.close()  # Menutup koneksi setelah keluar dari loop
    else:
        print("Koneksi ke MySQL gagal. Tidak dapat melanjutkan.")

# Menjalankan program utama
if __name__ == "__main__":
    main()