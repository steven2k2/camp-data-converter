import json
import unittest
import os
from src.converter import convert_html_to_json
from src.utils import load_json

class TestConverter(unittest.TestCase):

    def setUp(self):
        """Prepare test environment."""
        self.input_html = "../data/technicians.html"
        self.expected_json = "../data/expected_output.json"
        self.output_json = "../data/technicians.json"

    def test_conversion(self):
        """Test if HTML correctly converts to JSON."""
        # Run conversion
        convert_html_to_json(self.input_html, self.output_json)

        # Load output and expected data
        output_data = load_json(self.output_json)
        expected_data = load_json(self.expected_json)

        # Ensure output matches expected data
        self.assertEqual(output_data, expected_data, "Converted JSON does not match expected output.")

    def tearDown(self):
        """Clean up test artifacts."""
        if os.path.exists(self.output_json):
            os.remove(self.output_json)

if __name__ == "__main__":
    unittest.main()
