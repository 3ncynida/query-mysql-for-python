from koneksi import create_connection

# Fungsi untuk menampilkan daftar database
def list_databases():
    # Membuat koneksi ke MySQL
    mydb = create_connection()
    
    if mydb:  # Periksa apakah koneksi berhasil
        try:
            # Membuat cursor untuk menjalankan perintah SQL
            mycursor = mydb.cursor()
            
            # Menjalankan perintah untuk menampilkan semua database
            mycursor.execute("SHOW DATABASES")
            
            print("\nDaftar database yang tersedia:")
            for db in mycursor:
                print(f"- {db[0]}")  # Menampilkan nama database
        except Exception as e:
            print(f"Error saat menampilkan database: {e}")
        finally:
            mydb.close()  # Menutup koneksi
    else:
        print("Koneksi ke MySQL gagal.")
