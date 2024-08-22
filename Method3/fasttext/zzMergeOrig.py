with open('output_cleaned2.txt', 'r', encoding='utf-8') as file:
    # Read lines from the first file
    lines1 = file.readlines()

with open('HindiSentiWordnet.txt', 'r', encoding='utf-8') as file2:
    # Read lines from the second file
    lines2 = file2.readlines()

# Open the output file for writing
with open('HindiSentiWordnetv3.txt', 'w', encoding='utf-8') as output_file:
    # Iterate over corresponding lines from both files
    for line1, line2 in zip(lines1, lines2):
        # Remove newline characters from each line
        line1 = line1.strip()
        line2 = line2.strip()
        # Merge the lines and write to the output file
        output_file.write(f"{line2},{line1}\n")
