import os
from dotenv import load_dotenv

load_dotenv()

env_type = os.getenv('TYPE', 'development').upper()

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

config = env_mapping.get(env_type.lower(), env_mapping['development'])
