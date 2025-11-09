Traffic Congestion Analyzer

A Python-based project that analyzes traffic volume trends using historical traffic and weather data. This project uses PySpark for data processing and generates visualizations to understand traffic patterns by hour, day, and month.

Features

Reads traffic and weather data from CSV files.

Handles large datasets efficiently with PySpark.

Performs exploratory data analysis (EDA) on traffic volume.

Generates trend visualizations:

Hourly traffic trends.

Day-wise traffic trends.

Monthly traffic trends.

Saves charts in outputs/figures/.


💻 Technologies Used

Python 3.x

PySpark for distributed data processing

Matplotlib / Seaborn for visualizations

Pandas for lightweight data handling

Git for version control

📂 Project Structure
TrafficAnalyzer/
│
├── data/                   # Input dataset (CSV files)
├── outputs/                # Generated charts and visualizations
│   └── figures/
├── main.py                 # Main Python script to run analysis
├── README.md               # Project documentation
└── .venv/                  # Python virtual environment


🚀 Installation

Clone the repository:

git clone https://github.com/your-username/TrafficAnalyzer.git
cd TrafficAnalyzer


Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate     # Windows

How to Run
python main.py
Ensure your dataset CSV is in the data/ folder.

After running, charts will be saved in outputs/figures/.

📊 Example Output

Hourly traffic trend: outputs/figures/hourly_trend.png

Day-wise traffic trend: outputs/figures/daywise_trend.png

Monthly traffic trend: outputs/figures/monthly_trend.png
