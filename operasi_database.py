from koneksi import create_connection  # Importing the connection function

def use_database(mydb):
    """
    Function to select and use a specific database.
    Uses the connection provided from the calling function.
    """
    try:
        # Ask for the database name to use
        db_name = input("Masukkan nama database yang ingin digunakan: ")

        # Create a cursor to execute SQL commands
        mycursor = mydb.cursor()

        # Execute the USE DATABASE command
        mycursor.execute(f"USE {db_name}")
        print(f"Berhasil menggunakan database '{db_name}'.")
        return db_name  # Return the name of the database being used
    except Exception as e:
        print(f"Error saat menggunakan database: {e}")
        return None

def list_databases():
    """
    Function to list all available databases.
    """
    # Create connection to MySQL
    mydb = create_connection()
    
    if mydb:  # Check if the connection is successful
        try:
            # Create a cursor to execute SQL commands
            mycursor = mydb.cursor()
            
            # Execute the command to show all databases
            mycursor.execute("SHOW DATABASES")
            
            print("\nDaftar database yang tersedia:")
            for db in mycursor:
                print(f"- {db[0]}")  # Display database names
        except Exception as e:
            print(f"Error saat menampilkan database: {e}")
        finally:
            mydb.close()  # Close the connection
    else:
        print("Koneksi ke MySQL gagal.")

def create_database():
    """
    Function to create a new database.
    """
    db_name = input("Masukkan nama database yang ingin dibuat: ")
    
    # Create connection to the database
    mydb = create_connection()
    
    if mydb is None:
        return  # Stop the function if connection fails
    
    mycursor = mydb.cursor()
    
    try:
        mycursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' berhasil dibuat!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        mycursor.close()
        mydb.close()

def drop_database():
    """
    Function to drop an existing database.
    """
    # Create connection to MySQL
    mydb = create_connection()

    if mydb is None:
        return  # Stop the function if connection fails

    try:
        # Ask for the name of the database to delete
        db_name = input("Masukkan nama database yang ingin dihapus: ")

        # Create a cursor to execute SQL commands
        mycursor = mydb.cursor()

        # Execute the command to drop the database
        mycursor.execute(f"DROP DATABASE {db_name}")
        print(f"Database '{db_name}' berhasil dihapus!")
    except Exception as e:
        print(f"Error saat menghapus database: {e}")
    finally:
        mycursor.close()
        mydb.close()  # Close the connection after operation
