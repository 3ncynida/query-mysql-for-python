from koneksi import create_connection  # Modul koneksi
from operasi_database import list_databases, create_database, drop_database, use_database
from operasi_table import list_tables, create_table, drop_table, view_table_data, insert_data, delete_row  # Modul untuk operasi tabel

def get_current_database(mydb):
    """ Mendapatkan nama database yang sedang digunakan. """
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        return result[0] if result and result[0] else "None"
    except Exception as e:
        print(f"Error fetching current database: {e}")
        return "Error"


def display_menu():
    """ Menampilkan menu pilihan pengguna. """
    print("\nMenu:")
    print("========")
    print("Database")
    print("========")
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
    print("8. Insert data table")
    print("9. View data table")
    print("10. Delete data table")
    print("Ketik 'exit' untuk keluar")


def handle_database_commands(command, mydb):
    """ Menangani perintah terkait database. """
    if command == "1":
        list_databases()
    elif command == "2":
        create_database()
    elif command == "3":
        drop_database()
    elif command == "4":
        return use_database(mydb)
    return None


def handle_table_commands(command, mydb):
    """ Menangani perintah terkait tabel. """
    if command == "5":
        list_tables(mydb)
    elif command == "6":
        create_table(mydb)
    elif command == "7":
        drop_table(mydb)
    elif command == "8":
        insert_data(mydb)
    elif command == "9":
        view_table_data(mydb)
    elif command == "10":
        delete_row(mydb)


def main():
    """ Fungsi utama program. """
    mydb = create_connection()

    if mydb:
        current_db = get_current_database(mydb)

        while True:
            print(f"\nDatabase yang sedang digunakan: {current_db}")
            display_menu()
            
            command = input("Masukkan nomor perintah: ").strip()

            if command.lower() == "exit":
                print("Terima kasih! Program selesai.")
                break

            # Menangani perintah database
            if command in ["1", "2", "3", "4"]:
                current_db = handle_database_commands(command, mydb) or current_db

            # Menangani perintah tabel
            elif command in ["5", "6", "7", "8", "9", "10"]:
                if current_db != "None":
                    handle_table_commands(command, mydb)
                else:
                    print("Tidak ada database yang dipilih. Silakan pilih database terlebih dahulu.")
            else:
                print("Perintah tidak valid. Silakan masukkan nomor yang benar.")

        mydb.close()  # Menutup koneksi
    else:
        print("Koneksi ke MySQL gagal. Tidak dapat melanjutkan.")


if __name__ == "__main__":
    main()
