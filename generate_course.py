import pandas as pd
import json
from jinja2 import Environment, FileSystemLoader
import os

def generate_html_files():
    print("Starting course generation...")

    # Load data
    try:
        # Using encoding='utf-8' and proper quote handling
        df = pd.read_csv('course_data.csv', encoding='utf-8')
        print(f"Loaded {len(df)} rows from course_data.csv")
    except FileNotFoundError:
        print("Error: course_data.csv not found.")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    try:
        template = env.get_template('course_template.html')
        print("Loaded course_template.html")
    except Exception as e:
        print(f"Error loading template: {e}")
        return

    # Iterate through rows
    for row in df.itertuples(index=False):
        # Convert row to dictionary
        data = row._asdict()

        week_num = data.get('week_number')
        print(f"Processing Week {week_num}...")

        # Parse JSON fields
        json_fields = ['vocab_rows', 'idioms', 'warmup_questions', 'circuit_prompt_points']
        for field in json_fields:
            if field in data and isinstance(data[field], str):
                try:
                    # Clean up potential double-quote issues if pandas didn't catch them all,
                    # though standard CSV readers usually handle "" -> " inside fields.
                    # The CSV viewed previously seemed to be standard CSV format.
                    parsed_data = json.loads(data[field])
                    data[field] = parsed_data
                except json.JSONDecodeError as e:
                    print(f"  Warning: Error decoding JSON for field '{field}' in Week {week_num}: {e}")
                    print(f"  Problematic string: {data[field]}")
                    data[field] = [] # Fallback to empty list
            elif field not in data or pd.isna(data[field]):
                data[field] = []

        # Generate output filename
        try:
            week_int = int(week_num)
            output_filename = f"Week_{week_int:02d}.html"
        except (ValueError, TypeError):
            print(f"  Warning: Invalid week number: {week_num}. Skipping.")
            continue

        # Render template
        try:
            output_html = template.render(data)
        except Exception as e:
            print(f"  Error rendering template for Week {week_num}: {e}")
            continue

        # Write to file
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(output_html)

        print(f"  Generated {output_filename}")

if __name__ == "__main__":
    generate_html_files()
