import mysql.connector

def create_connection(host="localhost", user="root", password=""):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print("Koneksi berhasil!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None