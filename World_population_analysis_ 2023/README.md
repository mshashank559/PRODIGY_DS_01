# World Population Analysis (2023)

This project analyzes the population of countries around the world for the year 2023. Using population data and metadata from the World Bank, the goal is to visualize the top 20 most populated countries in 2023 using a bar chart. The project is implemented using Python with the `pandas`, `matplotlib`, and `seaborn` libraries.

## Project Structure

world_population_analysis_2023/ 
    ├── data/ 
        ├── API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv 
        ├── Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv 
        └── Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv 
    ├── population_analysis.py ← (main Python script) 
    ├── README.md ← (this file) 
    └── charts/ ← (optional: save plots here)


## Requirements

This project requires the following Python libraries:

- pandas
- matplotlib
- seaborn

You can install the required libraries using `pip`:

```bash
pip install pandas matplotlib seaborn


#-----------------------------------Data Sources-----------------------------------------------------------

Population Data: World Bank dataset (SP.POP.TOTL).

Metadata: Country and indicator metadata from World Bank.

#-------------------------------------Data Files:-----------------------------------------------------------

API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv: Contains population data for all countries.

Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv: Contains metadata about countries.

Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv: Contains metadata about the population indicator.

# -------------------------------------How to Run -----------------------------------------------------------

1.Clone this repository or download the files to your local machine.

2.Install the required Python libraries by running:

    pip install pandas matplotlib seaborn

3.Navigate to the project directory:

    cd world_population_analysis_2023

4.Run the Python script:

    python population_analysis.py

5.The bar chart of the top 20 most populated countries in 2023 will be saved in the charts/ directory and displayed on your screen.

#---------------------------------------------------Visualization-------------------------------------------------------------------

The script generates a bar chart showing the top 20 most populated countries in 2023, color-coded by income group. Population values are annotated on the bars for clarity.

#-----------------------------------------------------License-----------------------------------------------------------------------
This project is licensed under the MIT License - see the LICENSE file for details.
