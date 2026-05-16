import pandas as pd

# Charger le dataset
df = pd.read_csv("data/netflix_titles.csv")

# Analyse simple
summary = df.groupby("type").size().reset_index(name="count")

# Afficher
print(summary)

# Export CSV
summary.to_csv("output/summary.csv", index=False)

print("Pipeline completed successfully.")