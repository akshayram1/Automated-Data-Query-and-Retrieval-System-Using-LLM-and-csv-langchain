# Automated-Data-Query-and-Retrieval-System-Using-LLM-and-csv-langchain
# Automated-Data-Query-and-Retrieval-System-Using-LLM-and-csv-langchain
# CSV Data Query with LLM

This project provides a Streamlit web application that allows users to upload CSV files, generate MongoDB queries using LLM (Language Learning Model), and save query results. The application uses Google's Gemini API for query generation and MongoDB for data storage.

## Project Structure
```
├── data/
│   ├── sample_data.csv
│   ├── try.py
│   └── uploaded_file.csv
├── output/
│   ├── queries_generated.txt
│   ├── query_results.csv
│   └── query_results2.csv
├── src/
│   ├── config.py
│   ├── data_processor.py
│   ├── database.py
│   ├── init.py
│   ├── llm_query_generator.py
│   ├── main.py
│   └── streamlit_app.py
├── venv/
├── .env
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.8+
- MongoDB installed and running locally
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   
On Windows: .\venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following configuration:
```
# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/
DATABASE_NAME=product_database
COLLECTION_NAME=products

# Google Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key

# Application Configuration
DEBUG=True
CSV_CHUNK_SIZE=1000
```

## Running the Application

1. Ensure MongoDB / mongodb compass is running on your local machine:
```bash
mongod
```

2. Start the Streamlit application:
```bash
streamlit run src/streamlit_app.py
```

The application will be available at `http://localhost:8501`

## Usage

1. Upload a CSV file using the file uploader
2. Enter your query in natural language in the text input field
3. The application will generate a MongoDB query based on your input
4. Click "Execute Query" to run the query and view results
5. Download the query results as a CSV file using the download button

## Features

- CSV file upload and processing
- Natural language to MongoDB query conversion using Gemini LLM
- Automatic database cleanup after each session
- Query result export to CSV
- Duplicate removal from query results
- Interactive data visualization

## Important Notes

- The database is automatically deleted after each processing session for cleanup
- The application saves all generated queries in `output/queries_generated.txt`
- Query results are saved in `output/query_results2.csv`
- Make sure to keep your Gemini API key secure and never commit it to version control

## Troubleshooting

1. If MongoDB connection fails:
   - Verify MongoDB is running locally
   - Check MongoDB connection string in `.env`
   - Ensure MongoDB port (27017) is not blocked

2. If Gemini API calls fail:
   - Verify your API key in `.env`
   - Check your internet connection
   - Ensure you have sufficient API credits

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

# Automated-Data-Query-and-Retrieval-System-Using-LLM-and-csv-langchain
