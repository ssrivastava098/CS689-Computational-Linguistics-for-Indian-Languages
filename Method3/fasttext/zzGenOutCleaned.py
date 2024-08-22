with open('output_cleaned.txt', 'r', encoding='utf-8') as input_file:
    # Read each line from the input file
    data = input_file.readlines()

# Initialize an empty list to store cleaned lines
cleaned_lines = []

# Process each line in the data
for line in data:
    # Split the line by comma and keep only the first word
    cleaned_line = line.strip().split(',')[0]
    # Append the cleaned line to the list
    cleaned_lines.append(cleaned_line)


with open('output_cleaned2.txt', 'w', encoding='utf-8') as output_file:
    # Iterate over corresponding lines from both files
    for i in cleaned_lines:
        output_file.write(i+'\n')
