import os
from dotenv import load_dotenv
from mysql.connector import pooling, Error

load_dotenv()

env_type = os.getenv('TYPE', 'development').lower()

env_mapping = {
    'development': {
        'DB_HOST': os.getenv('DEV_DB_HOST'),
        'DB_PORT': int(os.getenv('DEV_PORT', 3306)),
        'DB_USER': os.getenv('DEV_DB_USER'),
        'DB_NAME': os.getenv('DEV_DB_NAME'),
        'DB_PASS': os.getenv('DEV_DB_PASS'),
        'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY_DEV'),
    },
    'production': {
        'DB_HOST': os.getenv('PROD_DB_HOST'),
        'DB_PORT': int(os.getenv('PROD_PORT', 3306)),
        'DB_USER': os.getenv('PROD_DB_USER'),
        'DB_NAME': os.getenv('PROD_DB_NAME'),
        'DB_PASS': os.getenv('PROD_DB_PASS'),
        'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY_PROD'),
    },
    'test': {
        'DB_HOST': os.getenv('TEST_DB_HOST'),
        'DB_PORT': int(os.getenv('TEST_PORT', 3306)),
        'DB_USER': os.getenv('TEST_DB_USER'),
        'DB_NAME': os.getenv('TEST_DB_NAME'),
        'DB_PASS': os.getenv('TEST_DB_PASS'),
        'JWT_SECRET_KEY': os.getenv('JWT_SECRET_KEY_TEST'),
    }
}

config = env_mapping.get(env_type, env_mapping['development'])

try:
    connection_pool = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size= 2,  
        pool_reset_session=True,  
        host=config['DB_HOST'],
        port=config['DB_PORT'],
        user=config['DB_USER'],
        password=config['DB_PASS'],
        database=config['DB_NAME']
    )
    print(f"Connection pool 'mypool' created with {connection_pool.pool_size} connections in {env_type} environment")
except Error as e:
    print(f"Error creating connection pool in {env_type} environment: {e}")
    raise e


def getConnection():
    try:
        connection = connection_pool.get_connection()
        if connection.is_connected():
            print(f"Successfully fetched connection from the pool in {env_type} environment")
            return connection
    except Error as e:
        print(f"Error fetching connection from the pool in {env_type} environment: {e}")
        raise e


def closeConnection(connection):
    if connection and connection.is_connected():
        connection.close() 
        print(f"Connection returned to the pool in {env_type} environment")


