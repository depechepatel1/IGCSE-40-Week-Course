import csv
import json
from jinja2 import Environment, FileSystemLoader
import os

def generate_html_files():
    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    try:
        template = env.get_template('template.html')
    except Exception as e:
        print(f"Error loading template: {e}")
        return
    
    # Load data using csv module (faster than pandas)
    try:
        with open('course_data.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            # Iterate through rows
            for row in reader:
                data = row.copy()

                # Parse JSON fields
                json_fields = ['vocab_rows', 'idioms', 'warmup_questions', 'circuit_prompt_points']
                for field in json_fields:
                    if field in data and data[field]:
                        try:
                            data[field] = json.loads(data[field])
                        except json.JSONDecodeError:
                            print(f"Error decoding JSON for field {field} in Week {data.get('week_number')}")
                            data[field] = []
                    elif field in data and not data[field]:
                        # Handle empty strings as empty lists
                        data[field] = []

                # Generate output filename
                try:
                    # Handle week_number robustly (e.g., "1", "1.0", 1)
                    week_val = data.get('week_number', '0')
                    week_num = int(float(week_val))
                    output_filename = f"Week_{week_num:02d}.html"
                    data['week_number'] = week_num  # Update for template use
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
                with open(output_filename, 'w', encoding='utf-8') as f_out:
                    f_out.write(output_html)

                print(f"Generated {output_filename}")

    except FileNotFoundError:
        print("Error: course_data.csv not found.")
        return

if __name__ == "__main__":
    generate_html_files()
