# 🌍 Global Health & Economic Analysis: Mortality Risk Prediction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)](https://streamlit.io/)

## 📌 Project Overview
This project investigates the complex interplay between macroeconomic stability and public health. By integrating datasets from the **World Bank** and **World Food Programme (WFP)**, I developed a machine learning pipeline to predict mortality risk across 200+ countries (2000–2025).

The core of this project is the **Silent Hunger Discovery Engine (SHDE)** logic, which identifies how food inflation and GDP fluctuations act as early warning signals for public health crises.

---

## 🚀 Key Achievements
- **High Accuracy:** Achieved **93.96% accuracy** using a Random Forest Classifier to categorize mortality risk (Low, Medium, High).
- **Advanced Engineering:** Implemented **Temporal Lag Features** to capture the 12-month delayed impact of food price shocks on mortality.
- **Actionable Insights:** Identified *Health Efficiency Index* and *GDP Stability* as the primary drivers of survival rates globally.

---

## 🛠️ Tech Stack
- **Languages:** Python (Pandas, NumPy)
- **Machine Learning:** Scikit-Learn (Random Forest, Label Encoding, Train-Test Split)
- **Visualization:** Seaborn, Matplotlib, Power BI
- **Deployment:** Streamlit (In Progress 🏗️)

---

## 📂 Project Structure
```text
├── data/
│   ├── raw/            # Original datasets from World Bank/WFP
│   └── processed/      # Cleaned & merged final_dataset.csv
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb          # Data wrangling & standardization
│   ├── 02_EDA_Visual_Insights.ipynb    # Statistical profiling & correlations
│   ├── 03_Feature_Engineering.ipynb    # Lag variables & risk binning
│   └── 04_Model_Training.ipynb         # Random Forest training & evaluation
├── models/             # Saved .pkl files for deployment
├── README.md           # Project documentation
└── requirements.txt    # List of dependencies

```
📊 Machine Learning Workflow
Target Engineering: Converted raw mortality rates into a balanced 3-tier risk classification system.

Temporal Modeling: Created 1-year lags for Economic indicators to model delayed physiological impacts.

Evaluation: Validated using Confusion Matrices and F1-Scores to ensure "High Risk" cases are captured with maximum precision.

🔍 Key Insights
The Shadow Effect: Economic shocks (Food Inflation) today show a measurable correlation with nutritional decline and mortality risk in the following year.

Resource Efficiency: High health expenditure does not always guarantee low mortality; the efficiency of spending is a stronger predictor.


👩‍💻 Author
SHANZAY KHAN Data Analyst | Public Health & Applied Analytics 
