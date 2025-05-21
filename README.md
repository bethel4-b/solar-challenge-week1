# Solar Challenge - Week 0
#### The project has the goal of researching, analyzing, and processing solar irradiance data across different regions. It will primarily undertake the tasks of cleaning, visualizing, and identifying trends/correlations that could help in the evaluation of solar potential and performance. This report is a digest of the data profiling, cleaning, and exploratory analysis steps taken for Benin within the general solar analytics exercise.

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/solar-challenge-week1.git
cd solar-challenge-week1
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---
# Streamlit Solar Dashboard

##  Overview
This app compares GHI, DNI, and DHI values across Benin, Togo, and Sierra Leone. It uses Streamlit for interactive visualization.

##  Structure
- `app/main.py`: Main dashboard
- `app/utils.py`: Data loading and cleaning
- `data/`: Cleaned CSVs (excluded from Git)

##  How to Run
```bash
streamlit run app/main.py
