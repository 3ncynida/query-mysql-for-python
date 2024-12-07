from tabulate import tabulate
import textwrap
from datetime import datetime

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
    while True:  # Loop agar bisa mencoba ulang jika ada error
        try:
            table_name = input("Masukkan nama tabel yang ingin dibuat: ")
            columns = input(
                "Masukkan kolom tabel dalam format (contoh: id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100)): "
            )
            cursor = mydb.cursor()
            query = f"CREATE TABLE {table_name} ({columns})"
            cursor.execute(query)
            print(f"Tabel '{table_name}' berhasil dibuat.")
            break  # Keluar dari loop jika berhasil
        except Exception as e:
            print(f"Error saat membuat tabel: {e}")
            retry = input("Apakah Anda ingin mencoba lagi? (y/n): ").strip().lower()
            if retry != 'y':  # Jika pengguna memilih tidak
                print("Operasi pembuatan tabel dibatalkan.")
                break


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


def validate_date(date_str):
    """
    Validasi apakah string sesuai format tanggal YYYY-MM-DD.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def insert_data(mydb):
    """
    Memasukkan data ke dalam tabel dengan validasi jumlah kolom dan nilai yang sesuai.
    """
    while True:
        try:
            table_name = input("Masukkan nama tabel untuk menambahkan data: ")

            # Memeriksa apakah pengguna ingin melihat kolom tabel terlebih dahulu
            columns = input(
                "Masukkan nama kolom yang akan diisi (contoh: id, name) atau ketik 'v' untuk melihat kolom tabel: "
            )
            
            if columns.lower() == 'v':
                cursor = mydb.cursor()
                query = f"DESCRIBE {table_name}"
                cursor.execute(query)
                
                # Ambil nama kolom, tipe data, dan informasi nullable
                fields = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
                print(tabulate(fields, headers=["Fields", "Type", "Nullable"], tablefmt="psql"))
                
                # Minta input kolom lagi setelah menampilkan
                columns = input("Masukkan nama kolom yang akan diisi (contoh: id, name): ")

            # Meminta nilai untuk kolom
            values = input("Masukkan nilai untuk kolom-kolom tersebut (contoh: 1, 'John Doe'): ")

            # Validasi jumlah kolom dan nilai
            column_count = len(columns.split(","))
            value_count = len(values.split(","))
            if column_count != value_count:
                print(f"Error: Jumlah kolom ({column_count}) dan nilai ({value_count}) tidak sesuai.")
                continue  # Kembali meminta input jika jumlah kolom dan nilai tidak sesuai

            # Perbaikan otomatis untuk nilai tanggal
            value_list = []
            for col, val in zip(columns.split(","), values.split(",")):
                col = col.strip()
                val = val.strip()
                if "tahun_terbit" in col.lower():  # Jika kolom bertipe DATE
                    val = val.strip("'")  # Hapus kutip jika ada
                    if not validate_date(val):  # Periksa format tanggal
                        print(f"Error: Nilai '{val}' untuk kolom '{col}' harus dalam format YYYY-MM-DD.")
                        break
                    val = f"'{val}'"  # Tambahkan kutip di sekitar nilai tanggal
                value_list.append(val)
            else:
                # Membuat query SQL untuk memasukkan data
                values = ", ".join(value_list)
                cursor = mydb.cursor()
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                cursor.execute(query)
                mydb.commit()
                
                print(f"Data berhasil dimasukkan ke tabel '{table_name}'.")
                break  # Keluar dari loop setelah data berhasil dimasukkan

        except Exception as e:
            print(f"Error saat memasukkan data: {e}")
            retry = input("Apakah Anda ingin mencoba lagi? (y/n): ").strip().lower()
            if retry != 'y':
                print("Operasi dibatalkan.")
                break


def view_table_data(mydb):
    """
    Menampilkan data dari tabel yang diminta.
    """
    try:
        table_name = input("Masukkan nama tabel untuk melihat data: ")

        # Membuat query SQL untuk mengambil data
        query = f"SELECT * FROM {table_name}"
        cursor = mydb.cursor()
        cursor.execute(query)

        # Ambil data dan nama kolom
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]  # Nama kolom dari tabel

        if rows:
            # Memotong teks panjang di kolom tertentu
            max_width = 50  # Maksimal lebar teks dalam satu baris
            formatted_rows = []
            for row in rows:
                formatted_row = [
                    textwrap.fill(str(value), width=max_width) if isinstance(value, str) else value
                    for value in row
                ]
                formatted_rows.append(formatted_row)

            # Menampilkan data dalam format tabel menggunakan tabulate
            print(tabulate(formatted_rows, headers=columns, tablefmt="psql"))
        else:
            print(f"Tabel '{table_name}' kosong atau tidak memiliki data.")
    except Exception as e:
        print(f"Error saat melihat data tabel: {e}")


def delete_row(mydb):
    """
    Menghapus baris dari tabel yang diminta berdasarkan kondisi tertentu.
    """
    try:
        table_name = input("Masukkan nama tabel untuk menghapus data: ")

        # Menanyakan kondisi untuk menghapus baris
        condition = input("Masukkan kondisi untuk menghapus baris (contoh: id=5): ")

        # Membuat query SQL untuk menghapus data berdasarkan kondisi
        query = f"DELETE FROM {table_name} WHERE {condition}"
        cursor = mydb.cursor()
        cursor.execute(query)

        # Commit perubahan
        mydb.commit()

        print(f"Baris berhasil dihapus dari tabel '{table_name}' dengan kondisi '{condition}'.")
    except Exception as e:
        print(f"Error saat menghapus data: {e}")
