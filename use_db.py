def use_database(mydb):
    """
    Fungsi untuk memilih dan menggunakan database tertentu.
    Menggunakan koneksi yang diberikan dari fungsi pemanggil.
    """
    try:
        # Meminta nama database yang ingin digunakan
        db_name = input("Masukkan nama database yang ingin digunakan: ")

        # Membuat cursor untuk menjalankan perintah SQL
        mycursor = mydb.cursor()

        # Menjalankan perintah USE DATABASE
        mycursor.execute(f"USE {db_name}")
        print(f"Berhasil menggunakan database '{db_name}'.")
        return db_name  # Mengembalikan nama database yang baru digunakan
    except Exception as e:
        print(f"Error saat menggunakan database: {e}")
        return None