from collections import defaultdict
import string
def get_top_words(filename, top_n=10):
    word_freq = defaultdict(int)
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                words = line.split()
                for word in words:
                    word_freq[word] += 1
        sorted_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
        print(f"Top {top_n} most frequent words:")
        for word, freq in sorted_freq[:top_n]:
            print(f"{word}: {freq}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
get_top_words("inputFile.txt")
