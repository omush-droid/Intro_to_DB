import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Replace with your MySQL password if set
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

    finally:
        # Safely close connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
