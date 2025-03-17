import json
from src.parser import parse_html

def convert_html_to_json(input_file, output_file):
    """Converts Basecamp-style HTML into structured JSON format."""
    data = parse_html(input_file)

    if data:
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"✅ JSON saved to {output_file}")
    else:
        print("❌ Failed to convert HTML to JSON.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python converter.py input.html output.json")
        sys.exit(1)

    convert_html_to_json(sys.argv[1], sys.argv[2])

