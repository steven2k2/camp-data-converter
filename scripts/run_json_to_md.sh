#!/bin/bash

# Define input and output files
INPUT_JSON="../data/output.json"
OUTPUT_MD="../data/report.md"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python is not installed. Please install Python and try again."
    exit 1
fi

# Run the JSON to Markdown conversion
echo "🔄 Converting JSON to Markdown..."
python3 ../json_to_md.py "$INPUT_JSON" "$OUTPUT_MD"

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo "✅ Markdown report saved to $OUTPUT_MD"
else
    echo "❌ Conversion failed. Please check for errors."
fi
