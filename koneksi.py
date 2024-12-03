def create_connection(host="localhost", user="root", password=""):
    import mysql.connector
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None