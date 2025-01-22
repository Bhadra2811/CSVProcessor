# import pandas as pd
# import threading
# from Lib.Utility import read_config, create_db_connection, create_table, insert_data, setup_logging

# def process_chunk(chunk, connection):
#     filtered_data = chunk[['id', 'name', 'email', 'city', 'status']].values.tolist()
#     insert_data(connection, filtered_data)

# def main():
#     setup_logging()
#     config = read_config()
#     connection = create_db_connection(config)

#     if connection:
#         create_table(connection)
#         chunksize = 1000
#         csv_file_path = config['CSV']['file_path']
        
#         threads = []
#         for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):
#             thread = threading.Thread(target=process_chunk, args=(chunk, connection))
#             threads.append(thread)
#             thread.start()

#         for thread in threads:
#             thread.join()

#         logging.info("All chunks have been processed.")
#         connection.close()

# if __name__ == "__main__":
#     main()
# ----------------------------------------------------------------------------
# import pandas as pd
# from Lib.Utility import insert_data
# from configparser import ConfigParser
# from Lib.Utility import create_db_connection, insert_data, read_config, setup_logging

# def main():
#     # Load configuration
#     config = read_config('Config/config.ini')
    
#     # Setup logging
#     setup_logging()

#     # Define the CSV file path and chunk size
#     csv_file_path = config['CSV']['file_path']
#     chunksize = 1000  # Adjust based on your file size and memory
    
#     # Read the CSV file in chunks and insert each chunk into the database
#     for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):
#         insert_data(chunk)

# if __name__ == "__main__":
#     main()


# def process_csv():
#     config = ConfigParser()
#     config.read('Config/config.ini')

#     file_path = config['CSV']['file_path']
#     chunksize = 1000  # Adjust the size based on your file

#     for chunk in pd.read_csv(file_path, chunksize=chunksize):
#         # Filter required columns
#         filtered_chunk = chunk[['id', 'name', 'email', 'city', 'status']]
        
#         # Insert the filtered data into PostgreSQL
#         insert_data(filtered_chunk)

# if __name__ == "__main__":
#     process_csv()
# ----------------------------------------------------------------------------
import pandas as pd
from Lib.Utility import create_db_connection, insert_data, read_config, setup_logging

def main():
    # Load configuration
    config = read_config('Config/config.ini')
    
    # Setup logging
    setup_logging()

    # Define the CSV file path and chunk size
    csv_file_path = config['CSV']['file_path']
    chunksize = 1000  # Adjust based on your file size and memory
    
    # Read the CSV file in chunks and insert each chunk into the database
    for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):
        insert_data(chunk)

if __name__ == "__main__":
    main()
