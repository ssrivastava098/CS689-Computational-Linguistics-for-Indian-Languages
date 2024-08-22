res = ""
with open('HindiSentiWordnet.txt', 'r', encoding='utf-8') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line by space
        parts = line.strip().split(' ')
        # Extract and print the first word
        temp = parts[4]
        res = res + "," + str(temp)

count=0;
for i in res:
    if (i==','):
        count+=1
print(count)