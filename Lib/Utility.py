import configparser
import logging
import psycopg2
from psycopg2 import Error
from datetime import datetime

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def create_db_connection(config):
    try:
        connection = psycopg2.connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config['Database']['password'],
            database=config['Database']['database']
        )
        logging.info("Database connection established.")
        return connection
    except Error as e:
        logging.error(f"Error connecting to the database: {e}")
        return None

def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        id SERIAL PRIMARY KEY,  -- Auto-increment ID
        name VARCHAR(255),
        email VARCHAR(255),
        city VARCHAR(255),
        status VARCHAR(255)
    )
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

def insert_data(connection, data):
    insert_query = """
    INSERT INTO user_data (name, email, city, status)
    VALUES (%s, %s, %s, %s)
    """
    cursor = connection.cursor()
    cursor.executemany(insert_query, data)
    connection.commit()
    cursor.close()

def setup_logging():
    logging.basicConfig(
        filename=f'process_log_{datetime.now().strftime("%Y%m%d")}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
