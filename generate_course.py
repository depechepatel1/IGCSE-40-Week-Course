import pandas as pd
import json
from jinja2 import Environment, FileSystemLoader
import os

def generate_html_files():
    # Load data
    try:
        df = pd.read_csv('course_data.csv')
    except FileNotFoundError:
        print("Error: course_data.csv not found.")
        return

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    try:
        template = env.get_template('template.html')
    except Exception as e:
        print(f"Error loading template: {e}")
        return
    
    # Iterate through rows
    for row in df.itertuples(index=False):
        # Convert row to dictionary
        data = row._asdict()
        
        # Parse JSON fields
        json_fields = ['vocab_rows', 'idioms', 'warmup_questions', 'circuit_prompt_points']
        for field in json_fields:
            if field in data and isinstance(data[field], str):
                try:
                    data[field] = json.loads(data[field])
                except json.JSONDecodeError:
                    print(f"Error decoding JSON for field {field} in Week {data.get('week_number')}")
                    data[field] = []

        # Generate output filename
        try:
            week_num = int(data.get('week_number', 0))
            output_filename = f"Week_{week_num:02d}.html"
        except ValueError:
            print(f"Invalid week number: {data.get('week_number')}")
            continue
        
        # Render template
        try:
            output_html = template.render(data)
        except Exception as e:
            print(f"Error rendering template for Week {week_num}: {e}")
            continue
        
        # Write to file
        with open(output_filename, 'w') as f:
            f.write(output_html)
        
        print(f"Generated {output_filename}")

if __name__ == "__main__":
    generate_html_files()
