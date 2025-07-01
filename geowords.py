import math

# Grid bounds 
LAT_MIN = 6.0
LAT_MAX = 38.0
LON_MIN = 68.0
LON_MAX = 97.0
GRID_SIZE = 3 / 111111  # 3 meters in degrees

# Load word list
try:
    with open("words.txt", "r") as f:
        WORDS = [w.strip() for w in f if 3 <= len(w.strip()) <= 6]
except FileNotFoundError:
    print("words.txt not found!")
    exit()

BASE = len(WORDS)

TOTAL_LAT_CELLS = int((LAT_MAX - LAT_MIN) / GRID_SIZE)
TOTAL_LON_CELLS = int((LON_MAX - LON_MIN) / GRID_SIZE)
TOTAL_CELLS = TOTAL_LAT_CELLS * TOTAL_LON_CELLS

if BASE ** 3 < TOTAL_CELLS:
    print(f"You need at least {math.ceil(TOTAL_CELLS ** (1/3))} words. Found only {BASE}.")
    exit()

def latlon_to_index(lat, lon):
    if not (LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX):
        raise ValueError("Coordinates out of bounds for India.")
    lat_idx = int((lat - LAT_MIN) / GRID_SIZE)
    lon_idx = int((lon - LON_MIN) / GRID_SIZE)
    return lat_idx * TOTAL_LON_CELLS + lon_idx

def index_to_latlon(index):
    lat_idx = index // TOTAL_LON_CELLS
    lon_idx = index % TOTAL_LON_CELLS
    lat = LAT_MIN + lat_idx * GRID_SIZE + GRID_SIZE / 2
    lon = LON_MIN + lon_idx * GRID_SIZE + GRID_SIZE / 2
    return lat, lon

def index_to_words(index):
    w1 = WORDS[index % BASE]
    w2 = WORDS[(index // BASE) % BASE]
    w3 = WORDS[(index // (BASE ** 2)) % BASE]
    return w1, w2, w3

def words_to_index(w1, w2, w3):
    try:
        i1 = WORDS.index(w1)
        i2 = WORDS.index(w2)
        i3 = WORDS.index(w3)
    except ValueError:
        raise ValueError("One or more words not found.")
    return i3 * BASE ** 2 + i2 * BASE + i1

def latlon_to_words(lat, lon):
    idx = latlon_to_index(lat, lon)
    return index_to_words(idx)

def words_to_latlon(w1, w2, w3):
    idx = words_to_index(w1, w2, w3)
    return index_to_latlon(idx)

# CLI
def main():
    print("India GeoWords Translator (3x3m grid)")
    print("1 → Coordinates → 3 Words")
    print("2 → 3 Words → Coordinates")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        try:
            lat = float(input("Enter Latitude: "))
            lon = float(input("Enter Longitude: "))
            words = latlon_to_words(lat, lon)
            print(f"({lat}, {lon}) → Words: {words}")
        except Exception as e:
            print(f"Error: {e}")
    elif choice == "2":
        try:
            w1 = input("Word 1: ").strip().lower()
            w2 = input("Word 2: ").strip().lower()
            w3 = input("Word 3: ").strip().lower()
            latlon = words_to_latlon(w1, w2, w3)
            print(f"Words ({w1}, {w2}, {w3}) → Coordinates: {latlon}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid input. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
