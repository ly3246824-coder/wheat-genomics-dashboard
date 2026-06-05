# 🌾 Wheat Genomics Dashboard

An interactive, data-driven Bioinformatics web application designed to analyze and visualize genomic data for wheat (*Triticum aestivum*). This project focuses on candidate genes responsible for harsh salinity tolerance, assisting researchers in gene selection and expression analysis.

---

## 🧬 Scientific Overview

Wheat has a highly complex hexaploid genome. Engineering cultivars for salinity tolerance requires tracking key functional transporters and transcription factors. This dashboard visualizes core gene candidates, including:

* **TaHKT1;5-D:** Crucial for root sodium exclusion.
* **TaNHX1 / TaNHX2:** Responsible for vacuolar sequestration.
* **TaSOS1:** Active in plasma membrane antiport dynamics.
* **Transcription Factors (DREB/WRKY):** Key molecular switches regulating downstream abiotic stress responses.

---

## 📊 Features & Functional Architecture

* **KPI Metrics Display:** Real-time summary statistics computing total genes analyzed, average gene length, and maximum tolerance capacity.
* **Interactive Genomic Data Table:** Tabular inspection of genetic profiles with client-side dynamic filtering capabilities.
* **Data Visualization Studio:** Driven by Plotly for rendering relative expression metrics and correlation insights (e.g., Gene Length vs. Salinity Tolerance Scores).

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3
* **Framework:** Streamlit (Web Architecture)
* **Data Engineering:** Pandas
* **Data Visualization:** Plotly Express

---

## 💻 Local Deployment & Setup

1. Clone this repository to your local directory
2. Install the required engineering dependencies:
```bash
pip install streamlit pandas plotly
