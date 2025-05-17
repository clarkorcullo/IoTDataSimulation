# IoT-Data-Simulation

## MO-IT148 - Applications Development and Emerging Technologies

This project is developed as part of the course **MO-IT148 - Applications Development and Emerging Technologies**. It demonstrates how to generate synthetic IoT sensor data for simulating real-time logistics tracking, which is essential for understanding smart supply chain systems and the role of IoT in modern technology.

---

## Project Overview
This project generates realistic, synthetic IoT data for logistics and cold chain monitoring. Each record simulates a package tracked by an IoT device, including:
- Geolocation (latitude, longitude)
- Environmental conditions (temperature, humidity)
- Vehicle speed
- Package status (in transit, at warehouse, delivered, delayed)
- Timestamp (within the last 24 hours)

The generated data is ideal for:
- Testing dashboards and analytics pipelines
- Prototyping IoT platforms
- Machine learning model development
- Educational demonstrations

---

## Features
- Simulates data for multiple devices and packages
- Realistic values for speed, temperature, humidity, and location
- Outputs data in both CSV and JSON formats
- Easy to extend for other IoT scenarios
- Well-commented code for learning and modification

---

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries: `pandas`, `numpy`, `json` (install with `pip install pandas numpy`)

### Running the Simulation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/clarkorcullo/IoTDataSimulation.git
   cd IoTDataSimulation
   ```
2. **Run the script:**
   ```bash
   python simulate_iot_data.py
   ```
3. **Output:**
   - `smart_tracking_data.csv` (tabular data)
   - `smart_tracking_data.json` (JSON array)

### Using Jupyter Notebook
1. Start Jupyter:
   ```bash
   jupyter notebook
   ```
2. Open `simulate_iot_data.ipynb` and run the cells to generate and view the data interactively.

---

## Example Output
| row_number | timestamp           | tracking_id | device_id | latitude   | longitude   | temperature | humidity | speed_kmph | status       |
|------------|---------------------|-------------|-----------|------------|-------------|-------------|----------|------------|--------------|
| 1          | 2025-05-17 08:56:08 | PKG7965     | DVC841    | 40.724469  | -73.986484  | 5.40        | 52.74    | 66.02      | at_warehouse |
| 2          | 2025-05-16 20:09:08 | PKG6416     | DVC346    | 40.718517  | -73.965087  | 2.57        | 38.67    | 56.10      | at_warehouse |
| ...        | ...                 | ...         | ...       | ...        | ...         | ...         | ...      | ...        | ...          |

---

## Contribution Guidelines
- Fork the repository and create a pull request for improvements.
- Add comments and documentation for any new features.
- Follow Python best practices for code style and structure.

---

## License
This project is for educational purposes as part of MO-IT148. Please credit the original authors and contributors if you use or modify this code.

---

## Contact
For questions or collaboration, please contact your course instructor or open an issue in this repository. 