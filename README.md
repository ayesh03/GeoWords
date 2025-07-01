# GeoWords Assignment

This project implements a reversible geolocation encoding system specifically for India using a 3-word human-readable format. The concept is similar to "What3Words" but is simplified and restricted to India. Each 3x3 meter grid cell within India's geographic boundary is assigned a unique combination of three words, which can be used to retrieve the original location approximately.

## Files Included

- `generate_words.py`: Script to generate a word list of 11,000 unique, short words (3–6 letters).
- `geowords.py`: The main translator to convert between (latitude, longitude) and (3 words).
- `words.txt`: Auto-generated file containing the words used for encoding.

---

## 1. `generate_words.py` – Word List Generator

This script creates a list of 11,000 unique pseudo-random English-like words using a predefined set of base nouns and syllable patterns.

### Highlights

- Uses random syllable-based patterns like CVC, CVCC, etc.
- Ensures word length between 3 and 6 characters.
- Includes 50 simple base nouns for memorability.
- Saves output to `words.txt`.

### Structure

```python
import random

BASE_NOUNS = [...]  # 50 common, memorable words

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
PATTERNS = ["CVC", "CVCV", "CVCC", "VCV", "VCVC", "CVCVC", "CVCCV", "CCVC", "CCVCV", "CVCVCV"]

def generate_word():  # Generates one word based on a random pattern
    ...

def generate_word_list(n=11000):  # Fills the set until it reaches 11,000
    ...

def save_to_file(words, filename="words.txt"):  # Saves to words.txt
    ...

if __name__ == "__main__":
    word_list = generate_word_list()
    save_to_file(word_list)
```

---

## 2. `geowords.py` – Geo Encoder/Decoder for India

This is the main application for encoding and decoding coordinates.

### Grid Definition

- **Latitudes**: 6.0 to 38.0 (covers India vertically)
- **Longitudes**: 68.0 to 97.0 (covers India horizontally)
- **Cell size**: Each grid cell represents a 3x3 meter square (approx. 0.000027° in lat/lon)

### Functions

```python
def latlon_to_index(lat, lon):  # Converts coordinates to a unique grid index
    ...

def index_to_latlon(index):  # Converts index back to the center of grid cell
    ...

def index_to_words(index):  # Converts index to a 3-word identifier
    ...

def words_to_index(w1, w2, w3):  # Converts 3 words back to a unique index
    ...

def latlon_to_words(lat, lon):  # End-to-end: (lat, lon) → (w1, w2, w3)
    ...

def words_to_latlon(w1, w2, w3):  # End-to-end: (w1, w2, w3) → (lat, lon)
    ...
```

### CLI Menu

```python
def main():
    print("India GeoWords Translator (3x3m grid)")
    print("1 → Coordinates → 3 Words")
    print("2 → 3 Words → Coordinates")
    ...
```

---

## Step-by-Step Usage

1. **Run `generate_words.py`** to create the word list:
   ```bash
   python generate_words.py
   ```

2. **Run `geowords.py`** to encode or decode:
   ```bash
   python geowords.py
   ```

3. **Option 1 – Encode Coordinates**
   ```
   Enter Latitude: 25.78976
   Enter Longitude: 74.32456
   Output: ('catr', 'ehi', 'poyl')
   ```

4. **Option 2 – Decode Words**
   ```
   Word 1: catr
   Word 2: ehi
   Word 3: poyl
   Output: (25.789764, 74.324554)
   ```

---

## Accuracy

- The encoding is **lossy within 3 meters** because it maps a 3x3m grid cell to its center.
- Precision is acceptable for most general-purpose location-based applications within India.
- Only supports locations inside India. Out-of-bound coordinates will raise an error.

---

## Word Requirements

- Requires **at least ~4700 unique words** to cover India's grid at 3-meter resolution.
- `generate_words.py` ensures at least 11,000 words are available.
- If you modify the boundaries or resolution, you must regenerate the word list accordingly.

---

## Customization

- To change the **grid resolution**, modify `GRID_SIZE = <meters> / 111111` in `geowords.py`.
- To change the **region of interest**, update `LAT_MIN`, `LAT_MAX`, `LON_MIN`, and `LON_MAX`.
- You can also adjust the base noun list or patterns in `generate_words.py`.

---

## Example Word Triplet

For the coordinates:
```
Latitude: 22.3215
Longitude: 70.7657
```

You may get:
```
Words: ('muki', 'yakh', 'eqax')
```

You can reverse it back to:
```
Coordinates: (22.321499, 70.765699)
```

---

