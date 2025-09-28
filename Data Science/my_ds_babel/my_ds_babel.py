import sqlite3
from io import StringIO
import os

def csv_to_sql(csv_content, database, table_name):
    """Creates SQL table and inserts data from CSV string."""
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        if isinstance(csv_content, StringIO):
            csv_content.seek(0)  # Reset cursor position to start of the stream
            data = [row.split(",") for row in csv_content.read().splitlines() if row.strip()]
        else:
            data = [row.split(",") for row in csv_content.splitlines() if row.strip()]

        if not data:
            print("CSV data is empty.")
            return

        column_names = data[0]
        num_cols = len(column_names)

        # Robust Column Type Detection
        column_types = ["TEXT"] * num_cols  # Initialize all to TEXT
        if len(data) > 1:
            for i in range(num_cols):
                all_ints = True
                all_floats = True
                for row in data[1:]:
                    if len(row) > i:  # check if the row has the correct number of columns
                        try:
                            int(row[i])
                        except (ValueError, IndexError):
                            all_ints = False
                            try:
                                float(row[i])
                            except (ValueError, IndexError):
                                all_floats = False
                                break  # No need to check other rows for this column
                    else:
                        all_ints = False
                        all_floats = False
                        break
                if all_ints:
                    column_types[i] = "INTEGER"
                elif all_floats:
                    column_types[i] = "REAL"

        create_table_stmt = f"CREATE TABLE IF NOT EXISTS {table_name} (" + \
                            ", ".join([f"\"{col}\" {type_}" for col, type_ in zip(column_names, column_types)]) + \
                            ");"
        cursor.execute(create_table_stmt)

        if len(data) > 1:
            placeholders = ", ".join(["?"] * num_cols)
            insert_stmt = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.executemany(insert_stmt, data[1:])

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

def sql_to_csv(database, table_name):
    """Converts SQL table to CSV string."""
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        csv_string = ",".join(column_names) + "\n"
        csv_string += "\n".join([",".join([str(value) for value in row]) for row in data])

        conn.close()
        return csv_string
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return ""

# Example usage
if __name__ == "__main__":
    # Tests omitted for brevity
    pass
...