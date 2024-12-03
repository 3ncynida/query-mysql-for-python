from koneksi import create_connection  # Mengimpor fungsi koneksi

def drop_database():
    # Membuat koneksi ke MySQL
    mydb = create_connection()

    if mydb is None:
        return  # Jika koneksi gagal, hentikan fungsi

    if mydb:  # Memeriksa apakah koneksi berhasil
        try:
            # Meminta nama database yang ingin dihapus
            db_name = input("Masukkan nama database yang ingin dihapus: ")

            # Membuat cursor untuk menjalankan perintah SQL
            mycursor = mydb.cursor()

            # Menjalankan perintah untuk menghapus database
            mycursor.execute(f"DROP DATABASE {db_name}")
            print(f"Database '{db_name}' berhasil dihapus!")

        except Exception as e:
            print(f"Error saat menghapus database: {e}")

        finally:
            mycursor.close()
            mydb.close()  # Menutup koneksi setelah operasi selesai