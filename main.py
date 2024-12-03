from koneksi import create_connection  # Modul koneksi
from create_db import create_database  # Modul untuk membuat database
from list_db import list_databases     # Modul untuk daftar database
from drop_db import drop_database      # Modul untuk menghapus database
from use_db import use_database        # Modul untuk memilih database
from operasi_table import list_tables, create_table, drop_table  # Modul untuk operasi tabel


def get_current_database(mydb):
    """
    Mendapatkan nama database yang sedang digunakan.
    """
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        return result[0] if result and result[0] else "None"  # Default 'None' jika tidak ada database
    except Exception as e:
        print(f"Error fetching current database: {e}")
        return "Error"


def main():
    # Membuat koneksi ke MySQL
    mydb = create_connection()

    if mydb:  # Periksa apakah koneksi berhasil
        while True:  # Loop tak terbatas
            # Mendapatkan nama database yang digunakan
            current_db = get_current_database(mydb)

            # Menampilkan menu
            print("\nMenu:")
            print("========")
            print("Database")
            print("========")
            print(f"Database yang sedang digunakan: {current_db}")
            print("1. List database")
            print("2. Create database")
            print("3. Delete Database")
            print("4. Use database")
            print("========")
            print("Tabel")
            print("========")
            print("5. List tables")
            print("6. Create table")
            print("7. Delete table")
            print("Ketik 'exit' untuk keluar")

            # Meminta input perintah dari pengguna
            command = input("Masukkan nomor perintah: ").strip()

            if command == "1":  # List database
                list_databases()

            elif command == "2":  # Buat database
                create_database()

            elif command == "3":  # Hapus database
                drop_database()


            elif command == "4":  # Gunakan database
                selected_db = use_database(mydb)
                if selected_db:
                    current_db = selected_db  # Perbarui nama database aktif


            elif command == "5":  # List tables
                if current_db != "None":
                    list_tables(mydb)
                else:
                    print("Tidak ada database yang dipilih. Silakan pilih database terlebih dahulu.")

            elif command == "6":  # Create table
                if current_db != "None":
                    create_table(mydb)
                else:
                    print("Tidak ada database yang dipilih. Silakan pilih database terlebih dahulu.")

            elif command == "7":  # Delete table
                if current_db != "None":
                    drop_table(mydb)
                else:
                    print("Tidak ada database yang dipilih. Silakan pilih database terlebih dahulu.")

            elif command.lower() == "exit":  # Keluar dari program
                print("Terima kasih! Program selesai.")
                break

            else:
                print("Perintah tidak valid. Silakan masukkan nomor yang benar.")

        mydb.close()  # Menutup koneksi setelah keluar dari loop
    else:
        print("Koneksi ke MySQL gagal. Tidak dapat melanjutkan.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
