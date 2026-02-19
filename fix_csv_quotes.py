import pandas as pd

# Read the CSV
df = pd.read_csv('course_data.csv')

# Function to clean cell content
def clean_quotes(text):
    if isinstance(text, str):
        # Replace literal double double-quotes with single double-quote
        # This fixes the issue where unquoted fields in CSV had "" instead of "
        return text.replace('""', '"')
    return text

# Apply to all columns. Use map() instead of applymap()
df = df.map(clean_quotes)

# Write back to CSV, ensuring proper quoting
df.to_csv('course_data.csv', index=False)
print("CSV fixed and saved.")
