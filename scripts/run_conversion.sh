#!/bin/bash

# Set input and output file paths
INPUT_FILE="../data/technicians.html"
OUTPUT_FILE="../data/output.json"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python is not installed. Please install Python and try again."
    exit 1
fi

# Run the conversion script
echo "🔄 Running Basecamp HTML to JSON conversion..."
python3 ../convert.py "$INPUT_FILE" "$OUTPUT_FILE"

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo "✅ Conversion completed! JSON saved to $OUTPUT_FILE"
else
    echo "❌ Conversion failed. Please check the script for errors."
fi
