import streamlit as st
import pandas as pd
from data_processor import DataProcessor
from llm_query_generator import LLMQueryGenerator

# Initialize Streamlit app
st.title("CSV Data Query with LLM")
st.write("Upload CSV, generate MongoDB query based on input, and save the results.")

# File uploader for CSV
csv_file = st.file_uploader("Upload CSV", type="csv")

if csv_file:
    # Save the uploaded file to a specific location for processing
    with open('data/uploaded_file.csv', 'wb') as f:
        f.write(csv_file.getbuffer())

    # Load CSV data to MongoDB
    data_processor = DataProcessor()
    data_processor.load_csv_to_mongodb('data/uploaded_file.csv')
    
    try:
        # User input for query
        user_input = st.text_input("Enter your query")

        if user_input:
            llm_generator = LLMQueryGenerator()
            
            # Fetch schema from MongoDB collection
            schema = data_processor.db_manager.collection.find_one()

            # Generate MongoDB query based on the user input and schema
            query = llm_generator.generate_query(user_input, schema)

            # Display generated query
            st.write("Generated MongoDB Query:")
            st.code(query)

            # Save generated query to file
            with open('output/queries_generated.txt', 'a') as f:
                f.write(f"User Input: {user_input}\n")
                f.write(f"Generated Query: {query}\n\n")

            # Option to execute query and save results
            if st.button("Execute Query"):
                output_file = 'output/query_results2.csv'
                
                # Execute the generated query and save results to CSV
                data_processor.execute_query_and_save(query, output_file)

                st.success(f"Query results saved to {output_file}")

                # Display download link for query results
                with open(output_file, 'rb') as f:
                    st.download_button(label="Download Query Results", data=f, file_name='query_results2.csv')

                # Display the unique contents of the CSV on the screen
                result_df = pd.read_csv(output_file)
                unique_df = result_df.drop_duplicates()  # Remove duplicate rows
                st.write("Unique Query Results:")
                st.dataframe(unique_df)

    finally:
        # Delete the database after each iteration
        data_processor.db_manager.client.drop_database(data_processor.db_manager.db.name)
        st.success("Database deleted after processing.")

        # Close the MongoDB connection
        data_processor.close()