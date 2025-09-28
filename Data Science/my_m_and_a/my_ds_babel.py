import sqlite3
import csv
from io import StringIO

def csv_to_sql(csv_data, db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        "Volcano Name" TEXT, 
                        "Country" TEXT, 
                        "Type" TEXT, 
                        "Latitude (dd)" REAL, 
                        "Longitude (dd)" REAL, 
                        "Elevation (m)" INTEGER)''')

    #  CSV data
    reader = csv.DictReader(csv_data)
    
    for row in reader:
        cursor.execute(f'''INSERT INTO {table_name} 
                           ("Volcano Name", "Country", "Type", "Latitude (dd)", "Longitude (dd)", "Elevation (m)") 
                           VALUES (?, ?, ?, ?, ?, ?)''', 
                           (row['Volcano Name'], row['Country'], row['Type'], 
                            row['Latitude (dd)'], row['Longitude (dd)'], row['Elevation (m)']))
    
    # commit 
    conn.commit()
    conn.close()




