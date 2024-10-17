import os
from data_processor import DataProcessor
from llm_query_generator import LLMQueryGenerator

def main():
    data_processor = DataProcessor()
    llm_generator = LLMQueryGenerator()

    # Load CSV data to MongoDB
    csv_file_path = 'data/sample_data.csv'
    data_processor.load_csv_to_mongodb(csv_file_path)

    # Get user input
    user_input = input("Enter your query: ")

    # Generate MongoDB query
    schema = data_processor.db_manager.collection.find_one()
    query = llm_generator.generate_query(user_input, schema)

    # Save query to file
    with open('output/queries_generated.txt', 'a') as f:
        f.write(f"User Input: {user_input}\n")
        f.write(f"Generated Query: {query}\n\n")

    # Execute query and save results
    output_file = 'output/query_results.csv'
    data_processor.execute_query_and_save(query, output_file)

    print(f"Query results saved to {output_file}")

    data_processor.close()

if __name__ == "__main__":
    main()