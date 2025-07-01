# generate_words.py

import random

# Base list of simple nouns
BASE_NOUNS = [
    "crow", "place", "whale", "tree", "stone", "river", "hill", "cloud", "star", "moon",
    "bird", "lake", "path", "road", "field", "sky", "wind", "rain", "sun", "leaf",
    "wave", "sand", "grass", "rock", "fish", "flower", "fire", "snow", "mist", "dust",
    "pond", "bush", "cliff", "valley", "plain", "brook", "stream", "ridge", "cave", "sea",
    "fog", "dew", "storm", "peak", "glade", "meadow", "swamp", "bay", "reef", "dune"
]

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
PATTERNS = ["CVC", "CVCV", "CVCC", "VCV", "VCVC", "CVCVC", "CVCCV", "CCVC", "CCVCV", "CVCVCV"]

def generate_word():
    pattern = random.choice(PATTERNS)
    return ''.join(random.choice(CONSONANTS) if c == 'C' else random.choice(VOWELS) for c in pattern)

def generate_word_list(n=11000):
    words = set(BASE_NOUNS)
    while len(words) < n:
        w = generate_word()
        if 3 <= len(w) <= 6:
            words.add(w)
    return sorted(words)

def save_to_file(words, filename="words.txt"):
    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")
    print(f"Generated {len(words)} words into {filename}")

if __name__ == "__main__":
    word_list = generate_word_list(11000)
    save_to_file(word_list)
