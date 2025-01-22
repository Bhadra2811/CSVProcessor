import pandas as pd
import logging  # Add this import
from Lib.Utility import create_db_connection, setup_logging, read_config, create_table, insert_data

def process_chunk(chunk, connection):
    # Filter and prepare data for insertion
    filtered_data = chunk[['name', 'email', 'city', 'status']].values.tolist()
    insert_data(connection, filtered_data)

def main():
    # Load configuration
    config = read_config('Config/config.ini')
    
    # Setup logging
    setup_logging()
    
    # Define the CSV file path and chunk size
    csv_file_path = config['CSV']['file_path']
    chunksize = 1000  # Adjust based on your file size and memory
    
    # Create a database connection
    connection = create_db_connection(config)
    
    if connection:
        # Create the table if it doesn't exist
        create_table(connection)
        logging.info("Database table verified/created successfully.")
        
        # Read the CSV file in chunks and insert each chunk into the database
        try:
            for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):
                process_chunk(chunk, connection)
                logging.info(f"Processed a chunk with {len(chunk)} records.")
        except Exception as e:
            logging.error(f"Error processing CSV: {e}")
        finally:
            # Close the database connection
            connection.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    main()
