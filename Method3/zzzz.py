import re

def clean_hindi_text(text):
    # Define a regular expression pattern to match Hindi characters
    hindi_pattern = re.compile(r'[\u0900-\u097F\s]+')  # Hindi Unicode range
    # Find all matches of Hindi text in the given string
    hindi_text = hindi_pattern.findall(text)
    # Join the found Hindi text with commas
    cleaned_text = ','.join(hindi_text)
    return cleaned_text

res = []
with open('output_formatted.txt', 'r', encoding='utf-8') as file:
    # Iterate through each line in the file
    for line in file:
        cleaned_text = clean_hindi_text(line)
        res.append(cleaned_text)

with open('output_cleaned.txt', 'w', encoding='utf-8') as output_file:
    for i in res:
        output_file.write(i)




# Open the input file
with open('output_cleaned.txt', 'r', encoding='utf-8') as input_file:
    # Read each line from the input file
    lines = input_file.readlines()

res = []
for i in lines:
    input_string = i
    elements = input_string.split(',')
    filtered_elements = [element for element in elements if len(element) <= 20]
    if not filtered_elements:
        filtered_elements.append("!!!")
    out = ','.join(filtered_elements)
    res.append(out)

with open('output_cleaned2.txt', 'w', encoding='utf-8') as output_file:
    for i in res:
        if(i == '!!!'):
            output_file.write('\n')
        else:
            output_file.write(i)

