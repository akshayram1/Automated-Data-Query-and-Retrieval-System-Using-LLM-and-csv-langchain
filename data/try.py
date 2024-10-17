# Let's load and inspect the CSV file first to understand its structure.
import pandas as pd

# Load the CSV file
file_path = 'data\sample_data.csv'
df = pd.read_csv(file_path)

# Show the first few rows and column names of the dataset

# Filter products with rating below 4.5, reviews greater than 200, and brand 'Nike' or 'Sony'
filtered_df = df[(df['Rating'] < 4.5) & 
                 (df['ReviewCount'] > 200) & 
                 (df['Brand'].isin(['Nike', 'Sony']))]

# Display the filtered products
print(filtered_df)