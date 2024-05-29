import os
import json

# Define the folder path containing the text files
folder_path = "/Users/bbc 2/business"

# Define the output JSONL file name
output_file = "output.jsonl"

# Function to read text from files and generate JSONL format
def generate_jsonl(folder_path, output_file):
    jsonl_data = []

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().strip()
                text2 = text.strip()[:100]
                # Append the text to jsonl_data
                jsonl_data.append({"input_text": text,"out_text":text2})

    # Write JSONL data to output file
    with open(output_file, 'w') as f:
        for line in jsonl_data:
            json.dump(line, f)
            f.write('\n')

# Call the function
generate_jsonl(folder_path, output_file)
