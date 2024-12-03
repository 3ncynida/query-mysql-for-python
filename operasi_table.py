from koneksi import create_connection

def list_tables(mydb):
    """
    Menampilkan daftar tabel dalam database yang sedang digunakan.
    """
    try:
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print("Tabel yang tersedia:")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("Tidak ada tabel dalam database ini.")
    except Exception as e:
        print(f"Error saat menampilkan tabel: {e}")


def create_table(mydb):
    """
    Membuat tabel baru di database yang sedang digunakan.
    """
    try:
        table_name = input("Masukkan nama tabel yang ingin dibuat: ")
        columns = input(
            "Masukkan kolom tabel dalam format (contoh: id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100)): "
        )
        cursor = mydb.cursor()
        query = f"CREATE TABLE {table_name} ({columns})"
        cursor.execute(query)
        print(f"Tabel '{table_name}' berhasil dibuat.")
    except Exception as e:
        print(f"Error saat membuat tabel: {e}")


def drop_table(mydb):
    """
    Menghapus tabel dari database yang sedang digunakan.
    """
    try:
        table_name = input("Masukkan nama tabel yang ingin dihapus: ")
        cursor = mydb.cursor()
        query = f"DROP TABLE {table_name}"
        cursor.execute(query)
        print(f"Tabel '{table_name}' berhasil dihapus.")
    except Exception as e:
        print(f"Error saat menghapus tabel: {e}")
