import json

def save_json(data, filename):
    """Saves dictionary data as JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"✅ JSON saved: {filename}")
    except Exception as e:
        print(f"❌ Error saving JSON: {e}")

def load_json(filename):
    """Loads JSON file and returns its content."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"❌ Error loading JSON: {e}")
        return None
