def my_csv_parser(csv_string, separator):

    lines = csv_string.strip().split('\n')
    
    result = []
    
    for line in lines:
        
        columns = line.split(separator)
        
        result.append(columns)
    
    return result

