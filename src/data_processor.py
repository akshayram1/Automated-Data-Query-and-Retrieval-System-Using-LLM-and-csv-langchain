import pandas as pd
from database import DatabaseManager
from config import CSV_CHUNK_SIZE

class DataProcessor:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def load_csv_to_mongodb(self, csv_file_path):
        for chunk in pd.read_csv(csv_file_path, chunksize=CSV_CHUNK_SIZE):
            records = chunk.to_dict('records')
            self.db_manager.insert_many(records)

    def execute_query_and_save(self, query, output_file):
        results = self.db_manager.execute_query(query)
        df = pd.DataFrame(results)
        df.to_csv(output_file, index=False)

    def close(self):
        self.db_manager.close_connection()