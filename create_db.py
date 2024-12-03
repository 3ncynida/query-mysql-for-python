from koneksi import create_connection  # Modul koneksi
import mysql.connector

def create_database():
    db_name = input("Masukkan nama database yang ingin dibuat: ")
    
    # Membuat koneksi ke database
    mydb = create_connection()
    
    if mydb is None:
        return  # Jika koneksi gagal, hentikan fungsi
    
    mycursor = mydb.cursor()
    
    try:
        mycursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' berhasil dibuat!")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        
    finally:
        mycursor.close()
        mydb.close()