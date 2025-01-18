import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_TYPES = {'development', 'production', 'test'}

TYPE = os.getenv('TYPE')

print(TYPE)

if TYPE not in ALLOWED_TYPES:
    raise ValueError(f"Invalid TYPE value: {TYPE}. Must be one of {ALLOWED_TYPES}.")

JWT_SECRET_KEY_DEV = os.getenv('JWT_SECRET_KEY_DEV')
JWT_SECRET_KEY_PROD = os.getenv('JWT_SECRET_KEY_PROD')
JWT_SECRET_KEY_TEST = os.getenv('JWT_SECRET_KEY_TEST')
ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', '').split(',')

if TYPE == 'development':
    JWT_SECRET_KEY = JWT_SECRET_KEY_DEV
elif TYPE == 'production':
    JWT_SECRET_KEY = JWT_SECRET_KEY_PROD
elif TYPE == 'test':
    JWT_SECRET_KEY = JWT_SECRET_KEY_TEST

constants = {
    'TYPE': TYPE,
    'JWT_SECRET_KEY': JWT_SECRET_KEY,
    'ALLOWED_ORIGINS': ALLOWED_ORIGINS
}
