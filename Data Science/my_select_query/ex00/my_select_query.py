import csv
from io import StringIO

class MySelectQuery:
    def __init__(self, csv_content: str):
        # Initialize by parsing the CSV content
        self.rows = []
        self.columns = []
        
        # Using StringIO to treat csv_content as a file object for csv reader
        csv_reader = csv.reader(StringIO(csv_content))
        
        # First row will be columns
        self.columns = next(csv_reader)
        
        # Remaining rows will be data
        self.rows = [row for row in csv_reader]
    
    def where(self, column_name: str, criteria: str):
        # Find the index of the column
        if column_name not in self.columns:
            return []
        
        column_index = self.columns.index(column_name)
        
        # Filter the rows based on the criteria in the specified column
        result = []
        for row in self.rows:
            if row[column_index] == criteria:
                result.append(','.join(row))
        
        return result
