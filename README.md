# Top 20 Most Populated Countries in 2023 – Population Analysis

This project presents a data visualization of the **top 20 most populated countries in 2023**, using data from the World Bank. The population figures are color-coded by income group to provide additional insights into economic classification.

## 📊 Tools Used

* **Python** for data processing and visualization
* **Pandas** for data manipulation
* **Matplotlib / Seaborn** for plotting
* **Power BI** for interactive dashboard development

## 🗂️ Data Sources

* [World Bank Open Data](https://data.worldbank.org/indicator/SP.POP.TOTL)

  * `API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv` – Population data
  * `Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv` – Country metadata (including income group)
  * `Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv` – Indicator metadata

## 🔍 Insights

* India has surpassed China in population in 2023.
* A majority of the top 20 most populated countries fall under the **Lower Middle Income** and **Upper Middle Income** categories.
* The **United States**, **Japan**, and **Germany** represent high-income countries among the top 20.

## 📈 Power BI Dashboard

In addition to the Python-based static visualization, an interactive dashboard has been created in **Power BI** to:

* Filter countries by **income group**, **region**, and **year**
* Analyze population trends over time
* Compare population distribution across continents

### 🖼️ Power BI Dashboard Preview

The Power BI dashboard delivers an intuitive and interactive interface, allowing users to:

* Visually explore the top 20 most populated countries using dynamic slicers.
* Drill down by **income group**, **geographic region**, or **individual countries**.
* View historical trends in population from 1960 to 2023.
* Interact with charts like bar graphs, line charts, and maps to understand demographic distribution and compare across nations.

This interactive format enhances data storytelling and makes complex patterns easier to understand, even for non-technical users.

## 📁 Project Structure

```
├── data/
│   ├── API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv
│   ├── Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv
│   └── Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv
├── visuals/
│   └── top_20_population_2023.png
├── dashboard/
│   └── PowerBI_PopulationDashboard.pbix
└── population_analysis.ipynb
```

## ✅ How to Run

1. Clone the repository.
2. Open `population_analysis.ipynb` in Jupyter Notebook.
3. Run the cells to generate the population bar chart.
4. Open `PowerBI_PopulationDashboard.pbix` in Power BI Desktop to explore the interactive dashboard.

## 📌 Requirements

* Python 3.8+
* pandas
* matplotlib
* seaborn
* Power BI Desktop (for `.pbix` file)

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

