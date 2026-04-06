# 🌍 Global Economic Mortality: Risk Prediction System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Live_Dashboard-Streamlit-red)](https://global-health-economic-analysis-4f3pemmspfmyta75xvj7n7.streamlit.app/)

## 🚀 Live Deployment
**Explore the Interactive Research Dashboard:** 👉 [**Global Mortality Intelligence Hub**](https://global-health-economic-analysis-4f3pemmspfmyta75xvj7n7.streamlit.app/)

---

## 📌 Project Overview
This project investigates the complex interplay between macroeconomic stability and public health outcomes. By integrating datasets from the **World Bank** and **World Food Programme (WFP)**, I developed a machine learning pipeline to predict mortality risk across 200+ countries (2010–2025).

The core of this project identifies how **Food Inflation** and **GDP fluctuations** act as early warning signals for public health crises, specifically focusing on the delayed physiological impact of economic shocks.

---

## 📂 Research & Development Workflow
The project is structured across **4 Specialized Notebooks**, covering the end-to-end Data Science Lifecycle:

1.  **`01_Data_Cleaning.ipynb`**: Wrangling multi-source data from World Bank (Health) and WFP (Economic).
2.  **`02_EDA_Visual_Insights.ipynb`**: Statistical profiling, correlation heatmaps, and outlier detection.
3.  **`03_Feature_Engineering.ipynb`**: Construction of **Temporal Lag Features** (12-month delay) and Risk Binning.
4.  **`04_Model_Training.ipynb`**: Training the **Random Forest Classifier** and evaluating via Confusion Matrices.

---

## 🛠️ Tech Stack
- **Engine:** Python (Pandas, NumPy, Scikit-Learn)
- **Modeling:** Random Forest Regression & Classification
- **Visualization:** Plotly Express (Interactive UI), Seaborn, Matplotlib
- **Deployment:** Streamlit Cloud

---

## 📊 Key Analytical Achievements
- **High Precision:** Achieved **93.96% accuracy** in categorizing Mortality Risk (Low, Medium, High).
- **Temporal Modeling:** Successfully modeled the **"Shadow Effect"**—showing how food price shocks today correlate with mortality outcomes in the following fiscal year.
- **Strategic Metrics:** Developed a *Health Efficiency Index* to measure the impact of GDP per capita vs. actual health outcomes.

---

## 📁 Repository Structure
```text
├── data/
│   └── processed/          # Unified research dataset (final_dataset.csv)
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_EDA_Visual_Insights.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   └── 04_Model_Training.ipynb
├── app.py                  # Streamlit Dashboard Source Code
├── mortality_model_final.pkl # Serialized Random Forest Model Bundle
├── requirements.txt        # Production dependencies (scikit-learn, plotly, etc.)
└── README.md
```

Gemini said
Bilkul Shanzay, ye raha tumhara Final Professional README. Maine ismein live link, tumhare charon notebooks ka structure, aur technical achievements ko AI-standard par set kar diya hai.

Bas GitHub par README.md mein Edit dabao, purana sab delete karo, aur ye Copy-Paste kar do:

Markdown
# 🌍 Global Economic Mortality: Risk Prediction System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Live_Dashboard-Streamlit-red)](https://global-health-economic-analysis-4f3pemmspfmyta75xvj7n7.streamlit.app/)

## 🚀 Live Deployment
**Explore the Interactive Research Dashboard:** 👉 [**Global Mortality Intelligence Hub**](https://global-health-economic-analysis-4f3pemmspfmyta75xvj7n7.streamlit.app/)

---

## 📌 Project Overview
This project investigates the complex interplay between macroeconomic stability and public health outcomes. By integrating datasets from the **World Bank** and **World Food Programme (WFP)**, I developed a machine learning pipeline to predict mortality risk across 200+ countries (2010–2025).

The core of this project identifies how **Food Inflation** and **GDP fluctuations** act as early warning signals for public health crises, specifically focusing on the delayed physiological impact of economic shocks.

---

## 📂 Research & Development Workflow
The project is structured across **4 Specialized Notebooks**, covering the end-to-end Data Science Lifecycle:

1.  **`01_Data_Cleaning.ipynb`**: Wrangling multi-source data from World Bank (Health) and WFP (Economic).
2.  **`02_EDA_Visual_Insights.ipynb`**: Statistical profiling, correlation heatmaps, and outlier detection.
3.  **`03_Feature_Engineering.ipynb`**: Construction of **Temporal Lag Features** (12-month delay) and Risk Binning.
4.  **`04_Model_Training.ipynb`**: Training the **Random Forest Classifier** and evaluating via Confusion Matrices.

---

## 🛠️ Tech Stack
- **Engine:** Python (Pandas, NumPy, Scikit-Learn)
- **Modeling:** Random Forest Regression & Classification
- **Visualization:** Plotly Express (Interactive UI), Seaborn, Matplotlib
- **Deployment:** Streamlit Cloud

---

## 📊 Key Analytical Achievements
- **High Precision:** Achieved **93.96% accuracy** in categorizing Mortality Risk (Low, Medium, High).
- **Temporal Modeling:** Successfully modeled the **"Shadow Effect"**—showing how food price shocks today correlate with mortality outcomes in the following fiscal year.
- **Strategic Metrics:** Developed a *Health Efficiency Index* to measure the impact of GDP per capita vs. actual health outcomes.

---

## 📁 Repository Structure
```text
├── data/
│   └── processed/          # Unified research dataset (final_dataset.csv)
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_EDA_Visual_Insights.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   └── 04_Model_Training.ipynb
├── app.py                  # Streamlit Dashboard Source Code
├── mortality_model_final.pkl # Serialized Random Forest Model Bundle
├── requirements.txt        # Production dependencies (scikit-learn, plotly, etc.)
└── README.md
```

🔍 Strategic Insights
The Lag Factor: Economic volatility (Inflation) has a measurable delayed impact on public health resilience.

Efficiency over Expenditure: National health spend is less predictive of survival than the efficiency of that spend relative to GDP stability.



Author: Shanzay Khan Data Analyst | Public Health & Applied Analytics Specialist

