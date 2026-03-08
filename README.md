# 📱 Smartphone Market Analysis

An end-to-end data analysis project on the Indian smartphone market — covering data cleaning, exploratory data analysis, and an interactive Streamlit dashboard for brand-wise and market-level insights.

---

## 🗂️ Project Structure

```
Smartphone-Market-Analysis/
│
├── smartphones (3).csv                  # Raw dataset (980 smartphones, 26 features)
├── Data_Cleaning_Start_To_End.ipynb     # Full data cleaning pipeline
├── EDA_on_smartphones_data.ipynb        # Exploratory Data Analysis notebook
├── app.py                               # Streamlit dashboard application
├── requirements.txt                     # Python dependencies
└── README.md
```

---

## 📊 Dataset Overview

| Property | Details |
|---|---|
| **Records** | 980 smartphones |
| **Features** | 26 columns |
| **Source** | Indian smartphone market |
| **Price Unit** | INR (Indian Rupee) |

**Key features include:** brand name, model, price (INR), rating, 5G/NFC/IR blaster support, processor details, RAM & ROM capacity, battery capacity, fast charging, screen size, resolution, refresh rate, camera specs, OS, and budget categorisation.

**Brands covered (46 total):** Apple, Samsung, OnePlus, Xiaomi, Realme, Redmi, POCO, Motorola, Vivo, OPPO, iQOO, Google, Sony, Nokia, Nothing, and many more.

**Budget categories:** Budget · Mid-Range · Premium · Flagship · Ultra Luxurious

---

## 🔍 Project Workflow

### 1. Data Cleaning (`Data_Cleaning_Start_To_End.ipynb`)
- Handled missing values and null entries
- Standardised column names and data types
- Removed duplicates and outliers
- Derived the `budget_categorisation` column from price ranges
- Ensured consistency across boolean fields (`has_5g`, `has_nfc`, `has_ir_blaster`)

### 2. Exploratory Data Analysis (`EDA_on_smartphones_data.ipynb`)
- Univariate analysis: price distribution, brand market share, OS breakdown
- Bivariate analysis: price vs. rating, 5G premium pricing, processor vs. price
- Camera analysis: rear/front MP distribution across brands
- Storage analysis: RAM & ROM capacity trends
- Correlation heatmaps for key numeric features

### 3. Interactive Dashboard (`app.py`)
A Streamlit web app with two main views:

**📊 Overview**
- *Univariate:* Budget category pie chart, avg. price per brand, top brands by model count, price histogram, 5G/NFC distribution, storage distribution, camera MP by brand, OS breakdown, avg. ratings per brand
- *Bivariate:* Brand-wise price distribution (brands with 10+ models), price vs. rating regression, 5G vs. non-5G pricing, processor brand vs. price, RAM/ROM vs. price scatter, camera correlation heatmap

**🏢 Brand Analysis**
- Filter by any of 46 brands
- Budget category distribution for the selected brand
- Price histogram, 5G/NFC/IR blaster breakdowns
- Processor, RAM/ROM, and camera distribution charts

**🔎 Model Specification**
- Select any individual model to view a full spec sheet

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kiranrawat-learning/Smartphone-Market-Analysis.git
cd Smartphone-Market-Analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core language |
| **Pandas** | Data manipulation & cleaning |
| **NumPy** | Numerical operations |
| **Matplotlib** | Static visualisations |
| **Seaborn** | Statistical visualisations |
| **Streamlit** | Interactive web dashboard |
| **Jupyter Notebook** | EDA & data cleaning |

---

## 📸 Dashboard Preview

> **Sidebar** → Choose between *Overview* (Univariate / Bivariate) and *Brand Analysis*. For Brand Analysis, further drill down to individual model specifications.

---

## 💡 Key Insights

- **Samsung** leads in model count; **Apple** and **Vertu** dominate average price
- **5G smartphones** command a significant price premium across all brands
- **Snapdragon** processors correlate with higher price points vs. MediaTek
- **12GB RAM / 256GB ROM** is the most common flagship configuration
- Only ~40% of smartphones in the dataset support **NFC**
- **Android** accounts for the vast majority of models; iOS limited to Apple

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, new features, or additional analyses.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---
## 📈 Tableau Dashboard

🔗 [View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/kiran.rawat3887/viz/SmartphonesDataQuickAnalysis/SMARTPHONESSUMMARY)
<img width="1879" height="990" alt="image" src="https://github.com/user-attachments/assets/95f67c4d-91d2-4122-9fbe-faaf8040b5b7" />




> 
## 👤 Author

**Kiran Rawat**
- GitHub: [@kiranrawat-learning](https://github.com/kiranrawat-learning)
