import json
import os
import psycopg2
import re

# read the config file
config_file = "secure/config.json"
with open(config_file) as f:
    config = json.load(f)

# connection parameters
db_name = config.get("DB_NAME")
db_user = config.get("DB_USER")
db_password = config.get("DB_PASSWORD")
db_host = config.get("DB_HOST")
table_name = config.get("TABLE_NAME")


def create_table():
    """
    Automates the first time creation of table in database.
    """
    try:
        # Establish a connection to the PostgreSQL server without specifying a database
        conn = psycopg2.connect(host=db_host, user=db_user, password=db_password)

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
        exists = cursor.fetchone()

        if not exists:
            # Database doesn't exist; ask the user to create it manually
            print(f"Please create the database named {db_name} as it doesn't exist.")
            return False
        else:
            try:
                # Establish a connection to the newly created database
                conn = psycopg2.connect(
                    host=db_host, database=db_name, user=db_user, password=db_password
                )

                # Create a cursor object to execute SQL queries
                cursor = conn.cursor()

                # Check if the table exists
                cursor.execute(f"SELECT to_regclass(%s)", (table_name,))
                table_exists = cursor.fetchone()

                if not table_exists[0]:
                    # Create the table if it doesn't exist
                    cursor.execute(
                        f"CREATE TABLE {table_name} (id serial PRIMARY KEY, username VARCHAR, password VARCHAR)"
                    )

                    # Commit the changes to the database
                    conn.commit()

                    print(f"Table {table_name} created successfully.")
                else:
                    print(f"Table {table_name} already exists.")

                # Close the cursor and the connection
                cursor.close()
                conn.close()

            except psycopg2.Error as e:
                print(f"\n\033[91mError creating table: {e}\033[0m")

    except psycopg2.Error as e:
        print(f"\n\033[91mError connecting to PostgreSQL: {e}\033[0m")


def validate_username(username):
    """
    Validates the format of the username.
    Checks for alphanumeric characters only.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    if not re.match("^[a-zA-Z0-9]+$", username):
        print(
            "\n\033[91mInvalid username format. Please use alphanumeric characters only.\033[0m"
        )
        return False
    return True


def validate_password(password):
    """
    Validates the complexity of the password.
    Checks if the password is at least 8 characters long.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) < 8:
        print("\n\033[91mPassword must be at least 8 characters long.\033[0m")
        return False
    return True


def login(username, password):
    """
    Performs the login operation.

    Args:
        username (str): The username to log in.
        password (str): The password associated with the username.

    Returns:
        bool: True if the login is successful, False otherwise.
    """
    try:
        # Data type validation
        if not isinstance(username, str) or not isinstance(password, str):
            print("\n\033[91mInvalid input data type.\033[0m")
            return False

        # Validate username format
        if not validate_username(username):
            return False

        # Validate password complexity
        if not validate_password(password):
            return False

        # Establish a connection to the database
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the query with parameters to prevent SQL injection
        query = f"SELECT * FROM {table_name} WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))  # security: Parameterized query

        # Fetch the result
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        # Check if a matching user was found
        if result is not None:
            return True

    except psycopg2.Error:
        # security: Avoid displaying specific error messages to the user
        pass

    return False


def register(username, password):
    """
    Performs the registration operation.

    Args:
        username (str): The username to register.
        password (str): The password to associate with the username.

    Returns:
        bool: True if the registration is successful, False otherwise.
    """
    try:
        # Data type validation
        if not isinstance(username, str) or not isinstance(password, str):
            print("\n\033[91mInvalid input data type.\033[0m")
            return False

        # Validate username format
        if not validate_username(username):
            return False

        # Validate password complexity
        if not validate_password(password):
            return False

        # Establish a connection to the database
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the query with parameters to prevent SQL injection
        query = f"INSERT INTO {table_name} (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))  # security: Parameterized query

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        return True

    except psycopg2.Error:
        # security: Avoid displaying specific error messages to the user
        pass

    return False


def app():
    """
    Runs the app.
    Allows users to login or register.
    """
    print(" ")
    print("===========================================")
    print("\033[1mWelcome to the Testing (Secure Version) Lab\033[0m")
    print("===========================================")

    choice = input("\n\033[1mSelect an option (1: Login, 2: Register): \033[0m")

    if choice == "1":
        print("\n--- \033[1mLogin\033[0m ---")
        username = input("Username: ")
        password = input("Password: ")

        if login(username, password):
            print("\n\033[92mLogin Successful!\033[0m")
            subprocess.run(["open", "secure/index.html"])
        else:
            print("\n\033[91mInvalid credentials\033[0m")

    elif choice == "2":
        print("\n--- \033[1mRegister\033[0m ---")
        username = input("Username: ")
        password = input("Password: ")

        if register(username, password):
            print("\n\033[92mRegistration Successful!\033[0m")
        else:
            print("\n\033[91mRegistration Failed!\033[0m")

    else:
        print("\033[91mInvalid choice.\033[0m")


# Call the function to create the database and table
create_table()

# Run the app
app()
