from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
DB_HOST = '217.21.94.103'
DB_NAME = 'u813060526_bgmi'
DB_USER = 'u813060526_bgmi'
DB_PASSWORD = '135@Hack'


# Connect to the MySQL Database
def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn


# Function to create the RoadOrg table if it doesn't exist
def create_table():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()

        # SQL query to create the RoadOrg table
        create_table_query = '''CREATE TABLE IF NOT EXISTS ServerAdmin (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    username VARCHAR(50) NOT NULL,
                                    password VARCHAR(50) NOT NULL
                                )'''

        # Execute the query to create the table
        cursor.execute(create_table_query)

        # Commit the changes and close the cursor/connection
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Failed to connect to the database.")


# API route to check username and password
@app.route('/check_credentials', methods=['POST'])
def check_credentials():
    # Get data from the POST request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Query the database to check for the username and password in the same row
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM ServerAdmin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    # Check if a result was found
    if result:
        return jsonify({"exists": True}), 200
    else:
        return jsonify({"exists": False}), 200



