import json
import sys

def json_to_markdown(json_file, md_file):
    """Converts a JSON work order export to a Markdown file."""
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        with open(md_file, "w", encoding="utf-8") as file:
            file.write("# Work Orders Report\n\n")

            for order in data.get("work_orders", []):
                file.write(f"## {order['id']} - {order['title']}\n")
                file.write(f"**Created At:** {order['created_at']}\n\n")
                file.write(f"**Client:** {order['client']}\n")
                file.write(f"**Location:** {order['location']}\n\n")

                # Assigned Technicians
                file.write("### Assigned Technicians\n")
                for tech in order.get("technicians", []):
                    file.write(f"- {tech}\n")
                file.write("\n")

                # Tasks
                file.write("### Tasks\n")
                for task in order.get("tasks", []):
                    file.write(f"- [ ] {task}\n")  # Markdown checklist
                file.write("\n")

                # Service Logs
                file.write("### Service Logs\n")
                for log in order.get("service_logs", []):
                    file.write(f"- {log}\n")
                file.write("\n---\n")

        print(f"✅ Markdown saved to {md_file}")

    except Exception as e:
        print(f"❌ Error converting JSON to Markdown: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python json_to_md.py input.json output.md")
        sys.exit(1)

    json_to_markdown(sys.argv[1], sys.argv[2])
