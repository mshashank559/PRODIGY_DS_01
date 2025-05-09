import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === 1. Load Data ===
DATA_DIR = "data"

df = pd.read_csv(os.path.join(DATA_DIR, "API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv"), skiprows=4)
meta_country = pd.read_csv(os.path.join(DATA_DIR, "Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv"))
meta_indicator = pd.read_csv(os.path.join(DATA_DIR, "Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_26346.csv"))

# === 2. Check Columns of meta_indicator ===
print(meta_indicator.columns)  # Check columns to identify the correct column name

# === 3. Extract Indicator Info Using INDICATOR_CODE ===
# Now we'll check the INDICATOR_CODE column for the matching code "SP.POP.TOTL"
indicator_info = meta_indicator.loc[meta_indicator["INDICATOR_CODE"] == "SP.POP.TOTL", "INDICATOR_NAME"].values[0]

# === 4. Filter Real Countries Only ===
real_countries = meta_country[meta_country["Region"].notna()]
df = df[df["Country Name"].isin(real_countries["TableName"])]

# === 5. Extract 2023 Population Data ===
pop2023 = df[["Country Name", "2023"]].dropna()
pop2023 = pop2023.merge(real_countries[["TableName", "Region", "IncomeGroup"]],
                        left_on="Country Name", right_on="TableName", how="left")

# === 6. Get Top 20 Countries ===
top20 = pop2023.sort_values(by="2023", ascending=False).head(20)

# === 7. Plot ===
sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

barplot = sns.barplot(
    y="Country Name", x="2023", hue="IncomeGroup",
    data=top20, palette="Set2"
)

# Add population labels on bars
for i, row in top20.iterrows():
    plt.text(row["2023"] + 5e6, i, f'{int(row["2023"] / 1e6)}M', va='center', fontsize=9)

# Chart title and labels
plt.title(f"Top 20 Most Populated Countries in 2023\n({indicator_info})", fontsize=15, weight='bold')
plt.xlabel("Population")
plt.ylabel("")
plt.xticks(ticks=[0, 500e6, 1000e6, 1500e6], labels=["0", "500M", "1B", "1.5B"])
plt.legend(title="Income Group", loc="lower right")
plt.tight_layout()

# === 8. Save chart to charts/ folder ===
CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)
plt.savefig(os.path.join(CHARTS_DIR, "top20_population_2023.png"))
plt.show()
