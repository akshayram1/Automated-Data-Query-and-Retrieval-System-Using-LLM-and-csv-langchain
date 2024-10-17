import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

class LLMQueryGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_query(self, user_input, schema):
        prompt = f"""
        Given the following MongoDB schema: {schema}
        Generate a MongoDB query for the following user request: {user_input}
        Return only the MongoDB query as a Python dictionary, without any explanation.
        """
        response = self.model.generate_content(prompt)

        # Clean the response by removing backticks and extra formatting
        cleaned_response = response.text.strip().strip('```python').strip('```')

        # Convert string to Python dictionary
        try:
            return eval(cleaned_response)
        except SyntaxError as e:
            print("Error parsing the query:", e)
            return None
