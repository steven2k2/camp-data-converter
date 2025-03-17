# Camp Data Converter

**Camp Data Converter** is a Python-based tool for extracting structured data from Basecamp HTML exports and converting it into **JSON** and **Markdown** formats. This allows for further transformations into CSV, Excel, or automation workflows.

### **Disclaimer**
This project is a **code example** intended for demonstration purposes only. **All data, company names, and individuals referenced within this repository are entirely fictitious.** Any resemblance to actual persons, living or dead, or real-world organizations is purely coincidental.

The use of **Nordic-style names, addresses, and data** is a **deliberate convention** chosen to ensure sample information is easily recognizable and does not inadvertently correspond to real entities in an Australasian context. This convention is purely aesthetic and does not imply any geographical or cultural affiliation.

This project is provided **as-is** with no guarantees or warranties. Use at your own discretion.


## 🚀 Features
- Parses **Basecamp HTML exports**
- Extracts **work orders, tasks, assigned technicians, and service logs**
- Converts to:
   - **JSON** (structured data output)
   - **Markdown** (human-readable reports)
- Easily extendable for **CSV, Excel, or Office 365 automation**

---

![Screenshot of HTML Data](./docs/images/convert.png)

---

## 📦 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/steven2k2/camp-data-converter.git
   cd camp-data-converter
   ```

2. Run the **setup script** to install dependencies:
   ```sh
   ./setup.sh
   ```

3. Activate the virtual environment:
   ```sh
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

---

## Usage

### **1️⃣ Convert an HTML export to JSON**
```sh
python convert.py data/sample_input.html output.json
```
- `sample_input.html` → Basecamp HTML export file
- `output.json` → JSON output file

Or use the **Bash script**:
```sh
./scripts/run_conversion.sh
```

---

### **2️⃣ Convert JSON to Markdown**
```sh
python json_to_md.py output.json report.md
```
- `output.json` → JSON output file from previous step
- `report.md` → Markdown output file

Or use the **Bash script**:
```sh
./scripts/run_json_to_md.sh
```

---

## Example Outputs

### **JSON Output**
```json
{
  "work_orders": [
    {
      "id": "WO-1042",
      "title": "Network Installation",
      "created_at": "2025-03-01 09:30:00",
      "client": "Acme Corp",
      "location": "123 Main Street, Sydney",
      "technicians": ["Michael Carter - Lead Technician", "Lisa Fernandez - Network Engineer"],
      "tasks": ["Install fibre-optic cabling", "Configure network routers"],
      "service_logs": ["Inspected site, existing infrastructure is compatible"]
    }
  ]
}
```

### **Markdown Output**
```
# Work Orders Report

## WO-1042 - Network Installation
**Created At:** 2025-03-01 09:30:00

**Client:** Acme Corp  
**Location:** 123 Main Street, Sydney  

### Assigned Technicians
- Michael Carter - Lead Technician
- Lisa Fernandez - Network Engineer

### Tasks
- [ ] Install fibre-optic cabling
- [ ] Configure network routers

### Service Logs
- Inspected site, existing infrastructure is compatible
```

---

## Future Enhancements
- **CSV and Excel export options**
- **Integration with Office 365 automation**
- **Web-based UI for interactive conversion**

---

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the **MIT License**.

---

### **Disclaimer**  
This project is a **code example** intended for demonstration purposes only. **All data, company names, and individuals referenced within this repository are entirely fictitious.** Any resemblance to actual persons, living or dead, or real-world organizations is purely coincidental.  

The use of **Nordic-style names, addresses, and data** is a **deliberate convention** chosen to ensure sample information is easily recognizable and does not inadvertently correspond to real entities in an Australasian context. This convention is purely aesthetic and does not imply any geographical or cultural affiliation.  

This project is provided **as-is** with no guarantees or warranties. Use at your own discretion.  
