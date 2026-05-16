import os
import pandas as pd


def generate_summary():

    df = pd.read_csv("data/netflix_titles.csv")

    summary = (
        df.groupby("type")
        .size()
        .reset_index(name="count")
    )

    os.makedirs("output", exist_ok=True)

    summary.to_csv("output/summary.csv", index=False)

    return summary


if __name__ == "__main__":

    result = generate_summary()

    print(result)
    print("Pipeline completed successfully.")