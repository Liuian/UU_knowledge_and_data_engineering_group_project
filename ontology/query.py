import pandas as pd

df = pd.read_csv("../data/wiki_db_cleaned_2.csv")

dup_titles = (
    df[df.duplicated(subset=["title"], keep=False)]
    .sort_values("title")
)

print(dup_titles[["title", "year","genre"]])