# Open the file
res = []
with open('HindiSentiWordnet.txt', 'r', encoding='utf-8') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line by space
        parts = line.strip().split(' ')
        # Extract and print the first word
        temp = parts[4].strip().split(',')
        res.append(temp[0])
