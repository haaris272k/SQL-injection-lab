import json
import psycopg2
import subprocess

# Read the config file
config_file = "config.json"
with open(config_file) as f:
    config = json.load(f)

# Connection parameters
db_name = config.get("DB_NAME")
db_user = config.get("DB_USER")
db_password = config.get("DB_PASSWORD")
db_host = config.get("DB_HOST")
table_name = config.get("TABLE_NAME")

# ANSI color codes
ANSI_RED = "\033[91m"
ANSI_GREEN = "\033[92m"
ANSI_RESET = "\033[0m"


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
        # Establish a connection to the database
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Construct the SQL query (vulnerable to SQL injection)
        query = f"SELECT * FROM {table_name} WHERE username = '{username}' AND password = '{password}'"

        # Execute the query
        cursor.execute(query)

        # Fetch the result
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        # Check if a matching user was found
        if result is not None:
            # Opening the 'login success page'
            subprocess.run(["open", "index.html"])
            return True

    except psycopg2.Error as e:
        print(
            f"\n{ANSI_RED}Error connecting to the database: {e.pgcode} - {e.pgerror}{ANSI_RESET}"
        )

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
        # Establish a connection to the database
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Construct the SQL query (vulnerable to SQL injection)
        query = f"INSERT INTO {table_name} (username, password) VALUES ('{username}', '{password}')"

        # Execute the query
        cursor.execute(query)

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        return True

    except psycopg2.Error as e:
        print(
            f"\n{ANSI_RED}Error connecting to the database: {e.pgcode} - {e.pgerror}{ANSI_RESET}"
        )

    return False


def app():
    """
    Runs the app.
    Allows users to login or register.
    """
    print(" ")
    print("================================================")
    print("\033[1mWelcome to the Testing (Vulnerable Version) Lab\033[0m")
    print("================================================")

    choice = input("\n\033[1mSelect an option (1: Login, 2: Register): \033[0m")

    if choice == "1":
        print("\n--- \033[1mLogin\033[0m ---")
        username = input("Username: ")
        password = input("Password: ")

        if login(username, password):
            print(f"\n{ANSI_GREEN}Login Successful!{ANSI_RESET}")
        else:
            print(f"\n{ANSI_RED}Invalid credentials{ANSI_RESET}")

    elif choice == "2":
        print("\n--- \033[1mRegister\033[0m ---")
        username = input("Username: ")
        password = input("Password: ")

        if register(username, password):
            print(f"\n{ANSI_GREEN}Registration Successful!{ANSI_RESET}")
        else:
            print(f"\n{ANSI_RED}Registration Failed!{ANSI_RESET}")

    else:
        print(f"{ANSI_RED}Invalid choice.{ANSI_RESET}")


# Run the app
app()



