import pandas as pd

df = pd.read_csv('course_data.csv')
print("--- WILF Content ---")
print(df.loc[0, 'wilf_content'])
print("\n--- Transcoded Input ---")
print(df.loc[0, 'transcoded_input'])
