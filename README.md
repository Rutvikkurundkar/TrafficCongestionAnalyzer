# Traffic Congestion Analyzer

A Python-based project that analyzes traffic volume trends using historical traffic and weather data. This project uses PySpark for data processing and generates visualizations to understand traffic patterns by hour, day, and month.

#Features

Reads traffic and weather data from CSV files.
Handles large datasets efficiently with PySpark.
Performs exploratory data analysis (EDA) on traffic volume.

#Generates trend visualizations:
Hourly traffic trends.
Day-wise traffic trends.
Monthly traffic trends.
Saves charts in outputs/figures/.


#💻 Technologies Used

1)Python 3.x
2)PySpark for distributed data processing
3)Matplotlib / Seaborn for visualizations
4)Pandas for lightweight data handling
5)Git for version control

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

<img width="1756" height="866" alt="image" src="https://github.com/user-attachments/assets/d85dc10c-470c-4626-9613-cb020c5bbe77" />


Day-wise traffic trend: outputs/figures/daywise_trend.png

Monthly traffic trend: outputs/figures/monthly_trend.png
