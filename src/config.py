import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'product_database')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'products')

# Google Gemini API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Application Configuration
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
CSV_CHUNK_SIZE = int(os.getenv('CSV_CHUNK_SIZE', 1000))