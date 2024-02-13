import csv
import random
import string
import os

def generate_random_csv(num_columns, column_types, file_name='random_data.csv', directory_path='None'):
    """
    Generates a random CSV file.

    :param bum_columns: List of column names for the CSV file.
    :param column_types: A list indicating the type of each column ('string' or 'float').
    :param file_name: Name of the CSV file.
    :param directory_path: Optional; the directory where the CSV file will be saved. If None, saves to the current working directory.
    """

    # Use the specified directory or fall back to the current working durectory
    save_path = os.path.join(directory_path if directory_path else os.getcwd(), file_name)

    # Generate column names
    column_names = []
    for i, col_type in enumerate(column_types, start=1):
        prefix = 'col_str' if col_type == 'string' else 'col_num'
        column_names.append(f'{prefix}_{i}')
    
    # Generate random data for each column
    rows = 1000 # Number of rows to generate
    data = []
    for _ in range(rows):
        row = []
        for col_type in column_types:
            if col_type == 'string':
                #Generate a random string of 10 characters
                random_string = ''.join(random.choices(string.ascii_letters, k=10))
                row.append(random_string)
            elif col_type == 'float':
                #Generate a random float
                random_float = random.uniform(1.0, 10000000.0)
                row.append(random_float)
        data.append(row)
    
    # Generate CSV file
    with open(save_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
        writer.writerows(data)
    
    return f'CSV file "{file_name}" generated successfully with {num_columns} columns.'

# example table
num_columns = 10
column_types = ['float','string','string','string','float','string','float','string','string','float']
generate_random_csv(num_columns, column_types)




