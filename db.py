import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('members.db')

# Create a cursor object
cursor = conn.cursor()

# Function to display table data
# Function to display table data
def display_table_data(table_name, header, query):
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print(f"\nContents of {table_name} Table")
        print(header)
        print("-" * len(header))
        for row in rows:
            print(row)
    else:
        print(f"No data available in {table_name} table.")

# Query to display data from the members table
display_table_data(
    "members",
    f"{'ID':<5} {'Name':<20} {'Email':<30} {'Level':<10}",
    "SELECT * FROM members;"
)

# Close the connection
conn.close()