# Function to populate the word dictionary
def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    return words

# Main Loop
if __name__ == "__main__":
    file_path = "dictionary.txt"
    words = []

    words = load_words_from_file(file_path)

    print(words)