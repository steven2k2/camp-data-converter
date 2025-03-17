import sys
import json
from bs4 import BeautifulSoup

def parse_html_to_json(html_file):
    """Parses a Basecamp-style HTML export and converts it into JSON format."""
    try:
        with open(html_file, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        data = {"work_orders": []}

        # Extract all work orders (h2 elements)
        for work_order in soup.find_all("h2"):
            work_order_data = {
                "id": work_order.text.split(":")[1].strip(),
                "title": work_order.text.split(":")[0].strip(),
                "created_at": work_order.find_next("p").text.replace("Created At: ", ""),
                "client": work_order.find_next("p").find_next("p").text.replace("Client: ", ""),
                "location": work_order.find_next("p").find_next("p").find_next("p").text.replace("Location: ", ""),
                "technicians": [],
                "tasks": [],
                "service_logs": []
            }

            # Extract assigned technicians
            tech_list = work_order.find_next("h3", text="Assigned Technicians").find_next("ul")
            if tech_list:
                work_order_data["technicians"] = [li.text for li in tech_list.find_all("li")]

            # Extract tasks
            task_list = work_order.find_next("h3", text="Tasks").find_next("ul")
            if task_list:
                work_order_data["tasks"] = [li.text for li in task_list.find_all("li")]

            # Extract service logs
            service_logs = work_order.find_next("h3", text="Service Logs").find_next("ul")
            if service_logs:
                work_order_data["service_logs"] = [li.text for li in service_logs.find_all("li")]

            data["work_orders"].append(work_order_data)

        return data

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    """Command-line execution."""
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.html output.json")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(f"Processing {input_file}...")
    json_data = parse_html_to_json(input_file)

    if json_data:
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"✅ Conversion successful! JSON saved to {output_file}")
    else:
        print("❌ Conversion failed.")

if __name__ == "__main__":
    main()
