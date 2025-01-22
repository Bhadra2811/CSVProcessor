# import configparser
# import logging
# import mysql.connector
# from mysql.connector import Error
# from datetime import datetime

# def read_config():
#     config = configparser.ConfigParser()
#     config.read('Config/config.ini')
#     return config

# def create_db_connection(config):
#     try:
#         connection = mysql.connector.connect(
#             host=config['Database']['host'],
#             user=config['Database']['user'],
#             password=config['Database']['password'],
#             database=config['Database']['database']
#         )
#         if connection.is_connected():
#             return connection
#     except Error as e:
#         logging.error(f"Error connecting to the database: {e}")
#         return None

# def create_table(connection):
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS user_data (
#         id INT PRIMARY KEY,
#         name VARCHAR(255),
#         email VARCHAR(255),
#         city VARCHAR(255),
#         status VARCHAR(255)
#     )
#     """
#     cursor = connection.cursor()
#     cursor.execute(create_table_query)
#     connection.commit()

# def insert_data(connection, data):
#     insert_query = """
#     INSERT INTO user_data (id, name, email, city, status)
#     VALUES (%s, %s, %s, %s, %s)
#     """
#     cursor = connection.cursor()
#     cursor.executemany(insert_query, data)
#     connection.commit()

# def setup_logging():
#     logging.basicConfig(
#         filename=f'process_log_{datetime.now().strftime("%Y%m%d")}.log',
#         level=logging.INFO,
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )
import psycopg2
from configparser import ConfigParser

def create_db_connection():
    config = ConfigParser()
    config.read('Config/config.ini')
    
    # Read PostgreSQL connection details
    host = config['PostgreSQL']['host']
    port = config['PostgreSQL']['port']
    user = config['PostgreSQL']['user']
    password = config['PostgreSQL']['password']
    database = config['PostgreSQL']['database']

    # Connect to PostgreSQL
    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection
