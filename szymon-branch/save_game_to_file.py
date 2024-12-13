import json

# Zapis do pliku
def save_file(filename, game_state):
    try:
        with open(filename, 'w') as file:
            json.dump(game_state, file, indent=4)
        print(f"Stan gry zapisano do pliku '{filename}'")
    except IOError as e:
        print(f"Błąd zapisu stanu gry do pliku: {e}")


# Odczyt z pliku
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            game_state = json.load(file)
        print(f"Stan gry odczytano z pliku '{filename}'")
        return game_state
    except IOError as e:
        print(f"Błąd odczytu stanu gry z pliku: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Błąd dekodowania JSON: {e}")
        raise