import json
import os

def inject_questions():
    try:
        with open('follow_up_questions.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("follow_up_questions.json not found.")
        return

    for i in range(1, 41):
        week_key = f"week_{i}"
        file_name = f"Week_{i:02d}.html"

        if not os.path.exists(file_name):
            print(f"File {file_name} not found, skipping.")
            continue

        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()

        week_data = data.get(week_key)
        if not week_data:
            print(f"No data for {week_key}, skipping.")
            continue

        # Prepare injection HTML
        s5_easy = week_data['section_5_transcoded']['easy']
        s5_hard = week_data['section_5_transcoded']['hard']

        s9_easy = week_data['section_9_listener_feedback']['easy']
        s9_hard = week_data['section_9_listener_feedback']['hard']

        # HTML template for the questions
        s5_html = f'''
        <div style="margin-top: 15px; padding-top: 10px; border-top: 1px dashed #bdc3c7; font-size: 0.9em;">
            <p style="margin: 0 0 5px 0;"><strong>Follow-up Questions:</strong></p>
            <ul style="margin: 0; padding-left: 20px;">
                <li style="margin-bottom: 5px;"><strong>(Easy)</strong> {s5_easy}</li>
                <li><strong>(Hard)</strong> {s5_hard}</li>
            </ul>
        </div>'''

        s9_html = f'''
        <div style="margin-top: 15px; padding-top: 10px; border-top: 1px dashed #bdc3c7; font-size: 0.9em;">
            <p style="margin: 0 0 5px 0;"><strong>Follow-up Questions:</strong></p>
            <ul style="margin: 0; padding-left: 20px;">
                <li style="margin-bottom: 5px;"><strong>(Easy)</strong> {s9_easy}</li>
                <li><strong>(Hard)</strong> {s9_hard}</li>
            </ul>
        </div>'''

        # Inject Section 5
        # Marker: border: 1px solid #1abc9c; border-left: 6px solid #1abc9c;
        marker_s5 = 'border: 1px solid #1abc9c; border-left: 6px solid #1abc9c;'
        start_s5 = content.find(marker_s5)

        modified = False

        if start_s5 != -1:
            # Find end of opening tag
            tag_end_s5 = content.find('>', start_s5)
            # Find next </div>
            div_end_s5 = content.find('</div>', tag_end_s5)

            if div_end_s5 != -1:
                # Check for existing injection to prevent duplication
                substring_s5 = content[tag_end_s5:div_end_s5]
                if "Follow-up Questions:" not in substring_s5:
                    content = content[:div_end_s5] + s5_html + content[div_end_s5:]
                    modified = True
                    # Adjust index for next search
                    # div_end_s5 has shifted, but we search for s9 separately
                else:
                    print(f"Week {i}: Section 5 questions already present.")
            else:
                print(f"Week {i}: Could not find closing div for Section 5")
        else:
            print(f"Week {i}: Could not find Section 5 marker")

        # Inject Section 9
        # Marker: border-left: 6px solid #3498db; background-color: #ebf5fb;
        marker_s9 = 'border-left: 6px solid #3498db; background-color: #ebf5fb;'
        start_s9 = content.find(marker_s9)

        if start_s9 != -1:
             # Find end of opening tag
            tag_end_s9 = content.find('>', start_s9)
            # Find next </div>
            div_end_s9 = content.find('</div>', tag_end_s9)

            if div_end_s9 != -1:
                substring_s9 = content[tag_end_s9:div_end_s9]
                if "Follow-up Questions:" not in substring_s9:
                    content = content[:div_end_s9] + s9_html + content[div_end_s9:]
                    modified = True
                else:
                    print(f"Week {i}: Section 9 questions already present.")
            else:
                print(f"Week {i}: Could not find closing div for Section 9")
        else:
             print(f"Week {i}: Could not find Section 9 marker")

        if modified:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(content)
            # print(f"Week {i}: Updated.")
            pass

    print("Injection process completed.")

if __name__ == '__main__':
    inject_questions()
