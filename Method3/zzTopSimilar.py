import fasttext.util

# Load pre-trained FastText model
#fasttext.util.download_model('hi', if_exists='ignore')  # download Hindi model if not already downloaded
ft = fasttext.load_model('cc.hi.300.bin')

def get_top_similar_words(word, k=7):
    # Get word vector for the given word
    word_vector = ft.get_word_vector(word)
    
    # Calculate cosine similarity between the word vector and all other word vectors
    similarity_scores = ft.get_nearest_neighbors(word, k=k+1)[1:]  # exclude the word itself
    
    # Extract similar words and their similarity scores
    similar_words = [sim[1] for sim in similarity_scores]
    
    return similar_words

# Example usage

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

haha = []
counter =1
for i in res:
    print(counter)
    counter+=1
    top_similar_words = get_top_similar_words(i)
    haha.append(top_similar_words)

# Open a file in write mode
with open('output.txt', 'w', encoding='utf-8') as file:
    # Iterate over each element in the list
    for element in haha:
        # Write the element to the file
        file.write(f"{element}\n")
